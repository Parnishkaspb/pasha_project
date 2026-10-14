from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, View
from django.http import HttpResponse, JsonResponse,  Http404, FileResponse
from django.conf import settings
import os
from .forms import LoginForm, RegisterForm, AddInformtionForm, newProjectsForm, findForm, InformationForm
from .help_func import *

def index(request):
    pass
    # return render(request, 'project/start.html')

def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            in_form = form.cleaned_data

            flag = True
            information = InformationAboutUser.objects.filter(login=in_form["login"]).filter(password=in_form["password"]).first()

            if information is None:
                flag = False
                context = {
                    'form': form,
                    'flag': flag,
                }
                return render(request, 'project/login.html', context=context)
            else:
                pass
                request.session['login'] = information.login
                request.session['name'] = information.name
                if not request.session.get('name', False):
                    return redirect("next_step_registration")
                else:
                    return redirect("main")

    else:
        form = LoginForm()
    return render(request, 'project/login.html', {'form': form})

def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            reg_form = form.cleaned_data

            flag_login = True
            flag_pass = True
            flag_promo = True
            
            if InformationAboutUser.objects.filter(login=reg_form["login"]).exists():
                flag_login = False
            
            if reg_form["password"] != reg_form["password_repeat"]:
                flag_pass = False

            checkpromo = InformationAboutUser.objects.filter(specialword=reg_form["specialwords"]).exists()
            if not checkpromo:
                flag_promo = False
            else:
                checkpromo = InformationAboutUser.objects.filter(specialword=reg_form["specialwords"]).values('id')
                checkpromo = checkpromo[0]["id"]

            if flag_login and flag_pass and flag_promo:
                new_user = InformationAboutUser(
                    login=reg_form["login"],
                    password=reg_form["password"],
                    checkpeople=0
                )
                new_user.save()

                your_user = InformationAboutUser.objects.filter(login=reg_form["login"]).values('id')
                your_user = your_user[0]["id"]
                new_friend = Friend(you= checkpromo, friend=your_user)
                new_friend.save()

                request.session['login'] = reg_form["login"]
                return redirect("next_step_registration")
            else:
                context = {
                    'form': form,
                    'flag_login': flag_login,
                    'flag_pass': flag_pass,
                    'flag_promo': flag_promo,
                }
                return render(request, 'project/register.html', context=context) 

    else:
        form = RegisterForm() 
    return render(request, 'project/register.html', {'form': form}) 

class CityAutocompleteView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        lists = City.objects.filter(title__istartswith=query).values('title')
        return JsonResponse(list(lists), safe=False)
        # query = request.GET.get('query', '')
        # cities = City.objects.filter(title__istartswith=query)
        # results = [{'id': city.pk, 'name': city.title} for city in cities]
        # return JsonResponse(results, safe=False)

class WhatDoAutocompleteView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        lists = What_Do.objects.filter(title__istartswith=query).values('title')
        return JsonResponse(list(lists), safe=False)
    
class KeywordsAutocompleteView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        lists = Keywords.objects.filter(title__istartswith=query).values('title')
        return JsonResponse(list(lists), safe=False)


def find_an_investor(request):
    if request.method == "POST":
        keyword = request.POST['keyword_input_hidden'].split(",")
        start_id = get_user_id(request.session.get('login', False))
        massiveWithYourFriends, massive = find_id(start_id)
        massive.insert(0, 'Мой проект')
        projects = []
        for i in range(0, len(massiveWithYourFriends)):
            project = newProjects.objects.filter(number = massiveWithYourFriends[i]['id'], endproject = True, on = True).values('pk', 'title', 'description', 'keywords', 'budget')
            if len(project) != 0:
                for j in range(0, len(project)):
                    projects.append({"owner": massiveWithYourFriends[i]['name'], 'project': project[j], "know": massive[i]})
        if len(keyword) != 0:
            masive = []
            flag = True
            for i in range(0, len(keyword)):
                if flag:
                    for j in range(0, len(projects)):
                        if keyword[i] in projects[j]['project']['keywords']:
                            masive.append(projects[j])
                    flag = False
                else:
                    for item in reversed(masive):
                        if keyword[i] not in item['project']['keywords']:
                            masive.remove(item)
            projects = masive
        return JsonResponse(projects, safe=False)
    else:
        context = {
            'picture': "static/assets/images/about.jpg"
        }
        return render(request, 'project/find_inv.html', context=context)


def create(request):
    if not request.session.get('login', False):
        return redirect("login")
    if not request.session.get('name', False):
        return redirect("next_step_registration")
    
    information = InformationAboutUser.objects.get(login=request.session.get('login', False))
    if request.method == "POST":
        print(request.POST)
        form = newProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            keywords_add_input = request.POST['keywords_add_input']
            keyword_input_hidden = request.POST['keywords']
            tmp_key = []

            for item in keywords_add_input:
                if item in keyword_input_hidden:
                    tmp_key.append(item)

            if len(tmp_key) != 0:
                for item in tmp_key:
                    key = Keywords(
                        title = item   
                        )
                    key.save()

            form = newProjectsForm(initial={'number': information.id})

    else:
        form = newProjectsForm(initial={'number': information.id})
        
    context = {
        'form': form,
        'picture': "static/assets/images/about.jpg",
        'type': 'create'
        }
    
    return render(request, 'project/create.html', context=context)

def main(request):
    if not request.session.get('login', False):
        return redirect("login")
    if not request.session.get('name', False):
        return redirect("next_step_registration")
    
    profile = InformationAboutUser.objects.filter(login=request.session.get('login')).values(
    'name', 'second_name', 'what_do', 'keywords', 'city', 'contact_information',
    'links', 'specialword', 'checkpeople', 'id').first()

    invite = Friend.objects.filter(friend=profile['id']).values('you').first()
    try:
        invite = InformationAboutUser.objects.get(pk=invite['you'])
    except:
        invite = 0

    context = {
        'name': profile['name'],
        'second_name': profile['second_name'],
        'what_do': profile['what_do'].split(','),
        'keywords': profile['keywords'].split(','),
        'city': profile['city'],
        'contact_information': profile['contact_information'],
        'links': profile['links'],
        'specialword': profile['specialword'],
        'checkpeople': profile['checkpeople'],
        'who_invite': invite,
        'pk': profile['id'],
        'picture': "static/assets/images/about.jpg"
    }
    return render(request, 'project/main.html', context=context)

def next_step_registration(request):
    if request.session.get('login', False):
        print('Login down')
        if not request.session.get('name', False):
            login = request.session.get('login', False)

            if request.method == "POST":
                form = AddInformtionForm(request.POST)
                
                if form.is_valid():
                    reg_form = form.cleaned_data
                    information = InformationAboutUser.objects.get(login=login)
                    information.name = reg_form["persona"]
                    information.second_name = reg_form["fio_psev"]
                    information.what_do = reg_form["whatdo_input_hidden"]
                    information.keywords = reg_form["keyword_input_hidden"]
                    information.city = reg_form["city_input_hidden"]
                    information.contact_information = reg_form["contact_information"]
                    information.links = reg_form["links"]
                    information.specialword = reg_form["specialwords"]
                    information.save()

                    tmoo_whatdo = reg_form["whatdo_input_hidden"].split(',')
                    tmoo_keywords = reg_form["keyword_input_hidden"].split(',')
    
                    keywords_add_input = reg_form['keywords_add_input'].split(',')
                    activity_add_input = reg_form['activity_add_input'].split(',')

                    tmp_what = []
                    tmp_key = []


                    for item in activity_add_input:
                        if item in tmoo_whatdo:
                            tmp_what.append(item)

                    for item in keywords_add_input:
                        if item in tmoo_keywords:
                            tmp_key.append(item)

                    if len(tmp_key) != 0:
                        for item in tmp_key:
                            print(item)
                            key = Keywords(
                                title = item   
                            )
                            key.save()

                    if len(tmp_what) != 0:
                        for item in tmp_what:
                            print(item)
                            what = What_Do(
                                title = item   
                            )
                            what.save()
                    

                    request.session['name'] = reg_form["persona"]
                    return redirect("main")
            else:
                form = AddInformtionForm()

            context = {
                'form': form,
            }

            return render(request, 'project/fill_your.html', context=context)
        else:
            return redirect("main")
    else:
        return redirect("login")
   
def find(request):
    if not request.session.get('login', False):
        return redirect("login")
    if not request.session.get('name', False):
        return redirect("next_step_registration")
    # print(people['people'])
    context = {
        'picture': "static/assets/images/about.jpg"
    }
    if request.method == "POST":

        start_id = get_user_id(request.session.get('login', False))
        
        start = time.time()
        
        massiveIDforName, massive = find_id(start_id)
        people = []
        for i in range(1, len(massiveIDforName)):
            print(massiveIDforName[i]['id'])
            search = InformationAboutUser.objects.filter(id=massiveIDforName[i]['id']).values('id', 'name', 'second_name', 'what_do', 'keywords', 'city', 'contact_information').first()
            people.append(json_string_people(search['id'], search['name'], search['second_name'], search['what_do'], search['keywords'], search['city'], search['contact_information'], massive[i-1]))


        end = time.time() - start
        print(f'Время выполнения скрипта: {end}')
        whatdo = request.POST['whatdo_input_hidden'].split(",")
        keyword = request.POST['keyword_input_hidden'].split(",")
        city = request.POST['city_input_hidden'].split(",")
        flag = True
        masive = []
        masive, flag = findPeople(whatdo, 'what_do', masive, flag, people)
        masive, flag = findPeople(keyword, 'keywords', masive, flag, people)
        masive, flag = findPeople(city, 'city', masive, flag, people)
        people = masive
        return JsonResponse(people, safe=False)
    
    return render(request, 'project/find.html', context=context)

def find_id(start_id):
    depth = 6
    yourfriend_DOWN = {'friend': []} # ID друзей для спуска
    find_friend_UP = {'friend': []} # ID друзей, которые знают тебя (Подъем)
    yourfriend_UPDOWN = {'friend': []} # ID друзей для сначала подъема потом спуска
    # ИСПОЛЬЗУЕТСЯ yourfriend_DOWN
    # ИСПОЛЬЗУЕТСЯ find_friend_UP 
    step = 0
    yourfriend_DOWN['friend'].append(json_string(step, start_id, sqlQuery_friend_nex(start_id)))
    start_len_massive = 0 
    finish_len_massive = 1
    step += 1
     
    while step <= depth:
        for i in range(start_len_massive, finish_len_massive):
            for j in yourfriend_DOWN['friend'][i]['people_friend']:
                yourfriend_DOWN['friend'].append(json_string(step, j,  sqlQuery_friend_nex(j)))
        start_len_massive = finish_len_massive
        finish_len_massive = len(yourfriend_DOWN['friend'])
        step += 1


    step = 0
    find_friend_UP['friend'].append(json_string(step, start_id, sqlQuery_you_nex(start_id)))
    start_len_massive = 0 
    finish_len_massive = 1
    step += 1
    while step <= depth:
        for i in range(start_len_massive, finish_len_massive):
            for j in find_friend_UP['friend'][i]['people_friend']:
                find_friend_UP['friend'].append(json_string(step, j,  sqlQuery_you_nex(j)))
        start_len_massive = finish_len_massive
        finish_len_massive = len(find_friend_UP['friend'])
        step += 1
    
    if len(find_friend_UP['friend']) != 1:
        start_len_massive = 1
        finish_len_massive = len(find_friend_UP['friend'])
        step = find_friend_UP['friend'][-1]['step']
        for do in range(start_len_massive, finish_len_massive):
            tmp_step = find_friend_UP['friend'][do]['step']
            start_tmp_id = find_friend_UP['friend'][do]['previous_id']
            yourfriend_UPDOWN['friend'].append(json_string(tmp_step, start_tmp_id, sqlQuery_friend_nex(start_tmp_id)))
            start_len_massive_tmp = len(yourfriend_UPDOWN['friend']) - 1
            finish_len_massive_tmp = len(yourfriend_UPDOWN['friend'])
            tmp_step += 1
            while tmp_step <= depth:
                for i_tmp in range(start_len_massive_tmp, finish_len_massive_tmp):
                    for j_tmp in yourfriend_UPDOWN['friend'][i_tmp]['people_friend']:
                        yourfriend_UPDOWN['friend'].append(json_string(tmp_step, j_tmp,  sqlQuery_friend_nex(j_tmp)))
                start_len_massive_tmp = finish_len_massive_tmp
                finish_len_massive_tmp = len(yourfriend_UPDOWN['friend'])
                tmp_step += 1

        
        unique_ids = set()
        unique_ids.add(start_id)
        result = []

        for item in yourfriend_UPDOWN['friend']:
            if item['previous_id'] not in unique_ids:
                unique_ids.add(item['previous_id'])
                result.append(item)
        yourfriend_UPDOWN['friend'] = result

        # print(yourfriend_UPDOWN['friend'])

    unique_ids = set()
    unique_ids.add(start_id)
    result = []

    for item in yourfriend_UPDOWN['friend']:
            if item['previous_id'] not in unique_ids:
                unique_ids.add(item['previous_id'])
                result.append(item)   
    
    yourfriend_DOWN['friend'], yourfriend_UPDOWN['friend'] = remove_duplicates(yourfriend_DOWN['friend'], yourfriend_UPDOWN['friend'])
    allfriend = yourfriend_DOWN['friend'] + yourfriend_UPDOWN['friend']
    unique_ids = set()
    # unique_ids.add()
    result = []
    for item in allfriend:
        if item['previous_id'] not in unique_ids:
            unique_ids.add(item['previous_id'])
            result.append(item) 
    allfriend = result
    massive_norm = []

    step = 1

    while step <= depth:
        for i in range(0, len(allfriend)):
            if allfriend[i]['step'] == step:
                massive_norm.append(allfriend[i])
                # print(allfriend[i])
        step += 1

    massive_for_path = []
    step = 1
    for i in range(0, len(allfriend[0]['people_friend'])):
        massive_for_path.append([start_id, allfriend[0]['people_friend'][i]])
    
    for i in range(0, len(massive_norm)):
        if len(massive_norm[i]['people_friend']) == 0:
            massive_for_path.append([massive_norm[i]['previous_id'], ''])
        else:
            for j in range(0, len(massive_norm[i]['people_friend'])):
                massive_for_path.append([massive_norm[i]['previous_id'], massive_norm[i]['people_friend'][j]])

    
    massive = []
    for i in range(0, len(massive_for_path)):
        if start_id in massive_for_path[i]:
            if massive_for_path[i][0] == start_id:
                tmp = [start_id, massive_for_path[i][1]]
            else:
                tmp = [start_id, massive_for_path[i][0]]
            massive.append(tmp)

    # print(massive)
    print()
    start_len = 0
    finish_len = len(massive)
    step = 2
    while step <= depth:
        for i in range(start_len, finish_len):
            # print(massive[i])
            if len(massive[i]) > 2:
                tmp_start_id = massive[i][len(massive[i])-1]
                # print(tmp_start_id)
            else:
                for j in range(0, len(massive[i])):
                    if massive[i][0] == start_id:
                        tmp_start_id = massive[i][1]
                    else:
                        tmp_start_id = massive[i][0]
            # print(tmp_start_id)
            for j in range(0, len(massive_for_path)):
                if tmp_start_id in massive_for_path[j] and massive_for_path[j] != massive[i] and start_id not in massive_for_path[j] and tmp_start_id in massive[i]:
                    
                    tmp = []
                    for q in range(0, len(massive[i])):
                        tmp.append(massive[i][q])
                    if massive_for_path[j][0] == tmp_start_id:
                        # print(massive_for_path[j][1])
                        if massive_for_path[j][1] not in massive[i]:
                            tmp.append(massive_for_path[j][1])
                        massive.append(tmp)
                    else:
                        # print(massive_for_path[j][0])
                        if massive_for_path[j][0] not in massive[i]:
                            tmp.append(massive_for_path[j][0])
                        massive.append(tmp)
                    # print(massive)
            start_len = finish_len
            finish_len = len(massive)
        step+=1
    # print(massive)

    massive = remove_duplicates_list(massive)
    # print(massive)
    massiveIDforName = [{"name": "Я", "id": start_id}]
    for item in massive:
        massiveIDforName.append({"name": get_user_name(item[len(item)-1]), "id": item[len(item)-1]})

    for i in range(0, len(massive)):
        for j in range(0, len(massive[i])):
            for q in range(0, len(massiveIDforName)):
                if massive[i][j] ==  massiveIDforName[q]['id']:
                    massive[i][j] = massiveIDforName[q]['name']

    return massiveIDforName, massive

def my_invest(request):
    if not request.session.get('login', False):
        return redirect("login")
    if not request.session.get('name', False):
        return redirect("next_step_registration")
    
    allMyProject = newProjects.objects.filter(number=get_user_id(request.session.get('login', False)), ).values('pk', 'title', 'description', 'keywords', 'budget', 'file', 'on')
    # print(allMyProject)
    context = {
        'allMyProject': allMyProject,
        'picture': "static/assets/images/about.jpg"
    }
    return render(request, 'project/myInvest-list.html', context=context)


def logout(request):
    request.session.flush()
    print(request.session.get('login'))
    print(request.session.get('name'))
    return redirect('login')

def download_file(request, file_id):
    file_model = newProjects.objects.get(id=file_id)
    file_path = file_model.file.path
    file_name = file_model.file.name
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response

def delete_project(request, id):
    project = newProjects.objects.get(pk=id)
    project.delete()
    return redirect("my_invest")


def edit_invest(request, id):
    information = newProjects.objects.get(pk=id)
    form = newProjectsForm(
        initial={
            'title': information.title,
            'description': information.description,
            'keywords': information.keywords,
            'budget': information.budget,
            'file': information.file,
            'number': information.number,
        }
    )
    context = {
        'form': form,
        'type': 'edit',
        'pk': id,
        'picture': "../static/assets/images/about.jpg",
        }
    
    if request.method == "POST":
        form = newProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            reg_form = form.cleaned_data
            information = newProjects.objects.get(pk=id)
            # information.title = reg_form["name"]
            # information.description = reg_form["fio_psev"]
            # information.keywords = reg_form["keyword_input_hidden"]
            # information.budget = reg_form["whatdo_input_hidden"]
            # information.city = reg_form["city_input_hidden"]
            # information.contact_information = reg_form["contact_information"]
            # information.links = reg_form["links"]
            # information.save()
            # return redirect("main")
        # else:
        #     context['error'] = 'Произошла ошибка! Пожалуйста, проверьте все данные! Или попробуйте позже!'
        #     return render(request, 'project/information.html', context=context)
    
    return render(request, 'project/create.html', context=context)

def edit_profile(request, id):
    information = InformationAboutUser.objects.get(pk=id)
    form = InformationForm(
        initial={
            'name': information.name,
            'fio_psev': information.second_name,
            'whatdo_input_hidden': information.what_do,
            'keyword_input_hidden': information.keywords,
            'city_input_hidden': information.city,
            'contact_information': information.contact_information,
            'links': information.links,
            }
    )
    context = {
        'title': 'Редактирование профиля',
        'button': 'Редактировать',
        'id': id,
        'error': '',
        'form': form,
        'picture': "../static/assets/images/about.jpg",
    }
    if request.method == "POST":
        form = InformationForm(request.POST)
        if form.is_valid():
            reg_form = form.cleaned_data
            information = InformationAboutUser.objects.get(pk=id)
            information.name = reg_form["name"]
            information.second_name = reg_form["fio_psev"]
            information.what_do = reg_form["whatdo_input_hidden"]
            information.keywords = reg_form["keyword_input_hidden"]
            information.city = reg_form["city_input_hidden"]
            information.contact_information = reg_form["contact_information"]
            information.links = reg_form["links"]
            information.save()
            return redirect("main")
        else:
            context['error'] = 'Произошла ошибка! Пожалуйста, проверьте все данные! Или попробуйте позже!'
            return render(request, 'project/information.html', context=context)
    # print(information)
    return render(request, 'project/information.html', context=context)



def work(request):
    context = {
        'error':'Данная страница в разработке',
        'picture': "static/assets/images/about.jpg",   
    }
    return render(request, 'project/work.html', context=context)