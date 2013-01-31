#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _  
from django import forms

from models import Category,Link,Post,Archive
from widgets import KindEditor  

class CategoryAdminForm(forms.ModelForm):
	class Meta:
		model = Category
		exclude = ('creator_id','creator_name','create_date','disabled',)
	
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'id_num', 'creator_name', 'create_date', 'disabled')
	form = CategoryAdminForm
	
	def save_model(self, request, obj, form, change):
		obj.creator_name = request.user.username
		obj.creator_id = request.user.id
		obj.disabled = 'N'
		obj.save()
		
class LinkAdminForm(forms.ModelForm):
	class Meta:
		model = Link
		exclude = ('creator_id','creator_name','disabled',)
	
class LinkAdmin(admin.ModelAdmin):
	list_display = ('displayorder', 'name', 'url', 'creator_name', 'create_date', 'disabled')
	form = LinkAdminForm
	
	def save_model(self, request, obj, form, change):
		obj.creator_name = request.user.username
		obj.creator_id = request.user.id
		obj.disabled = 'N'
		obj.save()
	
class PostAdminForm(forms.ModelForm):
	content   = forms.CharField(label=_(u"Content"), widget=KindEditor(attrs={'rows':15, 'cols':100}),required=True)
	class Meta:
		model = Post
		exclude = ('short_content','archive_date','creator_id','creator_name','create_date','disabled',)
		
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','category', 'closecomment', 'flag', 'creator_name', 'create_date', 'disabled')
	ordering = ('-id',)
	search_fields = ['title']
	form = PostAdminForm
	
	def save_model(self, request, obj, form, change):
		obj.creator_name = request.user.username
		obj.creator_id = request.user.id
		obj.disabled = 'N'
		if not change:
			obj.archive_date = time.strftime('%Y年%m月',time.localtime())
		if obj.content.find('</p>')==-1:
			obj.short_content = obj.content
		else :
			obj.short_content = obj.content[:obj.content.find('</p>')+4]
		obj.save()		
		if not change:
			category = obj.category
			category.id_num = category.id_num+1
			category.save()
			acount = Archive.objects.filter(creator_name=request.user.username,archive_date=obj.archive_date,disabled='N').count()
			if acount == 0:
				archive = Archive()
				archive.archive_date = obj.archive_date
				archive.archive_num = 1
				archive.creator_id = request.user.id
				archive.creator_name = request.user.username
				archive.disabled = 'N'
			else :
				archive = Archive.objects.filter(creator_name=request.user.username,archive_date=obj.archive_date,disabled='N')[0]
				archive.archive_num = archive.archive_num+1
			archive.save()
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Post, PostAdmin)
