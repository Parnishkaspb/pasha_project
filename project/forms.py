from django import forms
from .models import InformationAboutUser, newProjects
import re
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class LoginForm(forms.ModelForm):
    class Meta:
        model = InformationAboutUser
        # fields = '__all__' Для вывода всех полей из класса. Но лучше описывать все поля вручную
        fields = ['login', 'password']
        widgets = {
            'login': forms.TextInput(attrs={ 
                "id": 'login',
                "class": 'form-control',
                'required': True,
                "placeholder": 'Логин'
            }),
            'password': forms.PasswordInput(attrs={
                "id": 'password',
                "class": 'form-control',
                'required': True,
                "placeholder": 'Пароль',
                'autocomplet': "on"
            }),
        }

class RegisterForm(forms.Form):
    login = forms.CharField(max_length=30, required=True, label='Логин', widget=forms.TextInput(attrs={
        "id": 'login',
        "class": 'form-control',
        "placeholder": 'Введите логин'
    }))
    password = forms.CharField(max_length=50, required=True, label='Пароль', widget=forms.TextInput(attrs={
        "id": 'password',
        "class": 'form-control',
        "placeholder": 'Введите пароль'
    }))
    password_repeat = forms.CharField(max_length=50, required=True, label='Повторите пароль', widget=forms.TextInput(attrs={
        "id": 'password_repeat',
        "class": 'form-control',
        "placeholder": 'Подтвердите пароль'
    }))
    specialwords = forms.CharField(max_length=30, required=True, label='Логин', widget=forms.TextInput(attrs={
        "id": 'specialwords',
        "class": 'form-control',
        "placeholder": 'Введите промокод'
    }))
   
class AddInformtionForm(forms.Form):
    persona = forms.CharField(max_length=30, error_messages={"required": "Вы забыли ввести ваше имя"}, label='Имя', widget=forms.TextInput(attrs={
        "id": 'persona',
        "class": 'form-control',
        "placeholder": 'Введите имя'
    }))

    fio_psev = forms.CharField(max_length=50, help_text='Поле не является обязательным',required=False, label='Фамилия/Псевдоним', widget=forms.TextInput(attrs={
        "id": 'fio_psev',
        "class": 'form-control',
        "placeholder": 'Введите фамилию или псевдоним'
    }))


    whatdo_input = forms.CharField(max_length=50, required=False, label='Вид деятельности', widget=forms.TextInput(attrs={
        "id": 'whatdo_input',
        "class": 'form-control',
        "placeholder": 'Введите вид деятельности'
    }))

    whatdo_input_hidden = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "id": 'whatdo_input_hidden',
        "class": 'form-control',
        'name': 'whatdo_input_hidden',
        'type': 'hidden'
    }))

    keyword_input = forms.CharField(max_length=50, required=False, label='Ключевые слова', widget=forms.TextInput(attrs={
        "id": 'keyword_input',
        "class": 'form-control',
        "placeholder": 'Введите ключевые слова'
    }))

    keyword_input_hidden = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "id": 'keyword_input_hidden',
        "class": 'form-control',
        'name': 'keyword_input_hidden',
        'type': 'hidden'
    }))

    city_input = forms.CharField(max_length=50, required=False, label='Город', widget=forms.TextInput(attrs={
        "id": 'city_input',
        "class": 'form-control',
        "placeholder": 'Введите название города'
    }))

    city_input_hidden = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "id": 'city_input_hidden',
        "class": 'form-control',
        'name': 'city_input_hidden',
        'type': 'hidden'
    }))

    activity_add_input = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
        "type": "hidden",
        "id": 'activity_add_input',
    }))


    keywords_add_input = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
        "type": "hidden",
        "id": 'keywords_add_input',
    }))

    contact_information = forms.CharField(max_length=200, required=True, label='Контактная информация', widget=forms.TextInput(attrs={
        "id": 'contact_information',
        "class": 'form-control',
        "placeholder": 'Введите контактную информацию'
    }))
   
    links = forms.CharField(max_length=200, required=False, label='Внешние ссылки', widget=forms.TextInput(attrs={
        "id": 'links',
        "class": 'form-control',
        "placeholder": 'Вставьте ссылки на вашу компанию/на вас'
    }))

    specialwords = forms.CharField(max_length=200, required=True, label='Кодовое слово', widget=forms.TextInput(attrs={
        "id": 'specialwords',
        "class": 'form-control',
        "placeholder": 'Придумайте фразу для приглашения'
    }))

class newProjectsForm(forms.ModelForm):
    class Meta:
        model = newProjects
        # fields = '__all__' Для вывода всех полей из класса. Но лучше описывать все поля вручную
        fields = ['title', 'description', 'keywords', 'budget', 'file', 'number']
        widgets = {
            'title': forms.TextInput(attrs={ 
                "id": 'title',
                "class": 'form-control',
                'required': True,
                'label': 'Название проекта',
                "placeholder": 'Введите название проекта'
            }),
            'description': forms.Textarea(attrs={
                "id": 'description',
                "class": 'form-control',
                'required': True,
                'rows': 3, 
                'cols': 5,
                'label': 'Опишите ваш проект',
                "placeholder": 'Введите описание'
            }),
            'keywords': forms.HiddenInput(attrs={
                "id": 'keyword_input_hidden',
                "name": 'keyword_input_hidden',
                'required': True,
            }),
            'budget': forms.NumberInput(attrs={
                "id": 'budget',
                "class": 'form-control',
                'required': True,
                'label': 'Бюджет проекта',
                "placeholder": 'Введите бюджет проекта'
            }),
            # 'file': forms.FileInput(),
            'number': forms.HiddenInput(attrs={
                "id": 'number',
                'required': True,
            }),
        }

class findForm(forms.Form):
    what_do = forms.CharField(max_length=50, required=False, label='Вид деятельности', widget=forms.TextInput(attrs={
        "id": 'whatdo-input',
        "class": 'form-control',
        "placeholder": 'Введите вид деятельности'
    }))

    what_do_invisible = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
        "type": "hidden",
        "id": 'whatdo-input-hidden',
    }))

    keywords = forms.CharField(max_length=255, required=False, label='Ключевые слова', widget=forms.TextInput(attrs={
        "id": 'keyword-input',
        "class": 'form-control',
        "placeholder": 'Введите ключевые слова'
    }))

    keywords_invisible = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
        "type": "hidden",
        "id": 'keyword-input-hidden',
    }))

    city = forms.CharField(max_length=100, required=False, label='Город', widget=forms.TextInput(attrs={
        "id": 'city-input',
        "class": 'form-control',
        "placeholder": 'Введите город'
    }))

    city_invisible = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        "type": "hidden",
        "id": 'city-input-hidden',
    }))

class InformationForm(forms.Form):
    name = forms.CharField(max_length=30, error_messages={"required": "Вы забыли ввести ваше имя"}, label='Ваше имя', widget=forms.TextInput(attrs={
        "id": 'name',
        "class": 'form-control',
        "placeholder": 'Введите имя'
    }))

    fio_psev = forms.CharField(max_length=50, help_text='Поле не является обязательным',required=False, label='Фамилия/Псевдоним', widget=forms.TextInput(attrs={
        "id": 'fio_psev',
        "class": 'form-control',
        "placeholder": 'Введите фамилию или псевдоним'
    }))

    whatdo_input = forms.CharField(max_length=50, required=False, label='Вид деятельности', widget=forms.TextInput(attrs={
        "id": 'whatdo_input',
        "class": 'form-control',
        "placeholder": 'Введите вид деятельности'
    }))

    whatdo_input_hidden = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "id": 'whatdo_input_hidden',
        "class": 'form-control',
        'name': 'whatdo_input_hidden',
        'type': 'hidden'
    }))

    keyword_input = forms.CharField(max_length=50, required=False, label='Ключевые слова', widget=forms.TextInput(attrs={
        "id": 'keyword_input',
        "class": 'form-control',
        "placeholder": 'Введите ключевые слова'
    }))

    keyword_input_hidden = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "id": 'keyword_input_hidden',
        "class": 'form-control',
        'name': 'keyword_input_hidden',
        'type': 'hidden'
    }))

    city_input = forms.CharField(max_length=50, required=False, label='Город', widget=forms.TextInput(attrs={
        "id": 'city_input',
        "class": 'form-control',
        "placeholder": 'Введите название города'
    }))

    city_input_hidden = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "id": 'city_input_hidden',
        "class": 'form-control',
        'name': 'city_input_hidden',
        'type': 'hidden'
    }))

    contact_information = forms.CharField(max_length=200, required=True, label='Контактная информация', widget=forms.TextInput(attrs={
        "id": 'contact_information',
        "class": 'form-control',
        "placeholder": 'Введите контактную информацию'
    }))

    links = forms.CharField(max_length=200, required=False, label='Внешние ссылки', widget=forms.TextInput(attrs={
        "id": 'links',
        "class": 'form-control',
        "placeholder": 'Вставьте ссылки на вашу компанию/на вас'
    }))