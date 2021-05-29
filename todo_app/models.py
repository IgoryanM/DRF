from django.db import models

from siteusers.models import SiteUsers


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='название проекта')
    link = models.URLField(max_length=200, verbose_name='ссылка')
    users = models.ManyToManyField(SiteUsers, verbose_name='пользователи')


class Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='проект')
    user = models.ForeignKey(SiteUsers, on_delete=models.CASCADE, verbose_name='пользователь')
    text = models.TextField(max_length=300, verbose_name='текст заметки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создана')
    updated = models.DateTimeField(auto_now=True, verbose_name='изменена')
    is_active = models.BooleanField(db_index=True, default=True, verbose_name='активна')
