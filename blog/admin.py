#!/usr/bin/env python
# coding=utf-8

from django.contrib import admin

from models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "pub_time")    # name must same in models.py
    list_filter = ('pub_time',)
    list_per_page = 3            # 按每页3个显示，自动分页

admin.site.register(Article, ArticleAdmin)