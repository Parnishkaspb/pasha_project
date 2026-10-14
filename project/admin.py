from django.contrib import admin
from .models import  What_Do, City, Friend, Profession, Keywords, newProjects, InformationAboutUser
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'login') #Поля, которые будут видны в админке
#     search_fields = ('login',)


class InformationAboutUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'second_name', 'login', 'password','what_do', 'keywords', 'city', 'contact_information', 'links', 'checkpeople') #Поля, которые будут видны в админке
    search_fields = ('name', 'checkpeople') #Поиск в админке
    list_editable = ('name', 'second_name', 'checkpeople') #Корректировать что-то из админки непереходя в саму табличку
    list_filter = ('checkpeople',) #Фильтр в админке для быстрого поиска


# admin.site.register(User, UserAdmin)
admin.site.register(InformationAboutUser, InformationAboutUserAdmin)
admin.site.register(What_Do)
admin.site.register(City)
admin.site.register(Friend)
admin.site.register(Profession)
admin.site.register(Keywords)
admin.site.register(newProjects)
