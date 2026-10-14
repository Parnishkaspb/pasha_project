from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index),
    path('login', login, name='login'),
    path('main', main, name='main'),
    path('find_an_investor', find_an_investor, name='find_an_investor'),
    path('create', create, name='create'),
    path('register', registration, name='register'),
    path('next_step_registration', next_step_registration, name='next_step_registration'),
    path('find', find, name='find'),
    path('logout', logout, name='logout'),
    path('my_invest', my_invest, name='my_invest'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('edit_invest/<int:id>', edit_invest, name='edit_invest'),
    path('edit_profile/<int:id>', edit_profile, name='edit_profile'),
    path('autocompletecity/', CityAutocompleteView.as_view(), name='city_autocomplete'),
    path('autocompletewhatdo/', WhatDoAutocompleteView.as_view(), name='what_autocomplete'),
    path('autocompletekeyword/', KeywordsAutocompleteView.as_view(), name='keyword_autocomplete'),
    path('delete_project/<int:id>', delete_project, name='delete_project'),
    path('edit_invest/<int:id>', edit_invest, name='edit_invest'),
    path('work', work, name='work'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
