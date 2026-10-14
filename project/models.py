from django.db import models

class What_Do(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вид деятельности')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вид деятельности'

class City(models.Model):
    title = models.CharField(max_length=50, verbose_name='Город')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class InformationAboutUser(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Имя пользователя')
    second_name = models.CharField(max_length=150, verbose_name='Фамилия/Псевдоним пользователя')
    what_do = models.TextField(verbose_name='Вид деятельности')
    keywords = models.TextField(verbose_name='Ключевые слова')
    city = models.TextField(verbose_name='Город')
    contact_information = models.TextField(verbose_name='Контактная информация')    
    links = models.TextField(verbose_name='Внешние ссылки')
    # photo = models.FileField(upload_to='upload/photo/%Y/%m/%d/', verbose_name='Аватарка', blank=True)
    specialword = models.CharField(max_length=25, verbose_name='Секретная фраза')
    checkpeople = models.BooleanField(default=False, verbose_name='Проверенный аккаунт')
    login = models.CharField(max_length=100, verbose_name='Логин')
    password = models.CharField(max_length=150, verbose_name='Пароль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновление информации') 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Информация о пользователи'


class Friend(models.Model):
    you = models.IntegerField(verbose_name='ID человека')
    friend = models.IntegerField(verbose_name='ID друга')

    class Meta:
        verbose_name = 'Таблица друзей'


class Profession(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Вид деятельности')
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

class Keywords(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Ключевые слова')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'


class newProjects(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта', blank= True)
    keywords = models.TextField(verbose_name='Ключевые слова', blank=True)
    budget = models.IntegerField(verbose_name='Бюджет', blank=True)
    file = models.FileField(upload_to='upload/%Y/%m/%d/', verbose_name='Файл', blank=True)
    # file_picture = models.FileField(upload_to='upload/picture_for_file/%Y/%m/%d/', verbose_name='Обложка проекта', blank=True)
    number = models.IntegerField(verbose_name='ID владельца', default=0, blank=True)
    endproject = models.BooleanField(default=True, verbose_name='Показать проект')
    on = models.BooleanField(default=False, verbose_name='Проверенный проект')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'