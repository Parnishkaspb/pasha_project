from .models import *
import hashlib
import time 
import json
def json_string(tmp,id,massive):
    return {
        'step': tmp,
        'previous_id': id,
        'people_friend': massive,
    }

def json_string_people(id, name, second_name, what_do, keywords, city, contact_information, steps):
    return {
        'id': id,
        'name': name,
        'second_name': second_name,
        'what_do': what_do,
        'keywords': keywords,
        'city': city,
        'contact_information': contact_information,
        'know': steps
    }

def findPeople(what, name_what, massive, flag, people):
    if len(what) != 0:
        for i in range(0, len(what)):
            if flag:
                for j in range(0, len(people)):
                    if what[i] in people[j][name_what]:
                        massive.append(people[j])
                flag = False
            else:
                for item in reversed(massive):
                    if what[i] not in item[name_what]:
                        massive.remove(item)
    return massive, flag

def listToString_update(select_city):
    str1 = ""
    # number = 0
    for i in range(0, len(select_city)):
        # print(i)
        if i == len(select_city)-1:
            str1 += str(select_city[i])
        else:    
            str1 = str(select_city[i]) + ',' + str1
    return str1


def sqlQuery_friend_nex(what):
    massive = []
    for friend in Friend.objects.filter(you=what).values('friend'): 
        massive.append(friend['friend'])
    # print(f'Friend: {massive}')
    return massive

def sqlQuery_you_nex(what):
    massive = []
    for friend in Friend.objects.filter(friend=what).values('you'): 
        massive.append(friend['you'])
    # print(f'You: {massive}')
    return massive

    
def append_path(massive_for_path, i, previous_id):
    tmp = []
    for path in massive_for_path[i]:
        tmp.append(path)
    tmp.append(previous_id)
    massive_for_path.append(tmp)

def get_user_id(login):
    try:
        user = InformationAboutUser.objects.get(login=login)
        return user.id
    except InformationAboutUser.DoesNotExist:
        return None

def get_user_name(id):
    try:
        user = InformationAboutUser.objects.get(pk=id)
        return user.name
    except InformationAboutUser.DoesNotExist:
        return None

def sha256_hash(data):
    data_bytes = data.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(data_bytes)
    return sha256.hexdigest()


def remove_duplicates(data1, data2):
    unique_data = []
    seen_values = set()

    for item in data1 + data2:
        item_tuple = tuple((k, v) for k, v in item.items() if k != 'people_friend')
        if item_tuple not in seen_values:
            seen_values.add(item_tuple)
            unique_data.append(item)

    unique_data1 = unique_data[:len(data1)]
    unique_data2 = unique_data[len(data1):]
    return unique_data1, unique_data2

def remove_duplicates_list(lst):
    unique_items = []
    for item in lst:
        if item not in unique_items and item[len(item)-1] != '':
            unique_items.append(item)
    return unique_items