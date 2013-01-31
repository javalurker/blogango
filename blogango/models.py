# -*- coding: utf-8 -*- 
from django.db import models

from taggit.managers import TaggableManager

class Archive(models.Model):
	'''
	归档
	archive_date: 归档时间，类型为char
	archive_num: 归档时间，int型
	creator_id: 创建人id，int型
	creator_name: 创建人name，char型
	disabled: 是否可用，char型，N表示可用，Y表示不可用
	'''
	archive_date = models.CharField(max_length=10,blank=True)
	archive_num = models.IntegerField()
	creator_id = models.IntegerField()
	creator_name = models.CharField(max_length=30)
	disabled = models.CharField(max_length=1,default='N')

class Link(models.Model):
	'''
	链接
	displayorder: 排序，int型，数字越小越靠前
	name: 名字，char型，用于显示名称
	url: 链接的url，char型
	creator_id: 创建人id，int型
	creator_name: 创建人name，char型
	create_date: 创建日期，datetime型
	disabled: 是否可用，char型，N表示可用，Y表示不可用
	'''
	displayorder = models.IntegerField()
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	creator_id = models.IntegerField()
	creator_name = models.CharField(max_length=30)
	create_date = models.DateTimeField(auto_now=True)
	disabled = models.CharField(max_length=1,default='N')
	
class Category(models.Model):
	'''
	类别
	name: 名称，CharField,主键
	id_num: 帖子数量，类型为IntegerField
	content: 内容，TextField
	creator_id: 创建人id，int型
	creator_name: 创建人name，char型
	create_date: 创建日期，datetime型
	disabled: 是否可用，char型，N表示可用，Y表示不可用
	'''
	name = models.CharField(max_length=30,primary_key=True)
	id_num = models.IntegerField(default=0)
	content = models.TextField(blank=True)
	creator_id = models.IntegerField()
	creator_name = models.CharField(max_length=30)
	create_date = models.DateTimeField(auto_now=True)
	disabled = models.CharField(max_length=1,default='N')
	
	def __unicode__(self):#加这个就好了
		return self.name
		
class Post(models.Model):
	'''
	帖子
	flag: 类型，char型，定义4种类型，1：文字；2：图片；3：声音；4：影像
	title: 标题，char型
	content: 文字内容，类型为text
	short_content: 文字内容(用于列表展现)，类型为text
	img_content: 图片内容，类型为text
	music_name: 声音名称，类型为char
	music_songer: 演唱，类型为char
	music_title: 专辑，类型为char
	media_url: 媒体链接，类型为char
	closecomment: 是否结帖，类型char，Y：结帖；N：不结
	tags: 标签，类型char
	edit_time: 编辑时间，类型datetime
	archive_date: 归档时间，类型为char
	creator_id: 创建人id，int型
	creator_name: 创建人name，char型
	create_date: 创建日期，datetime型
	disabled: 是否可用，char型，N表示可用，Y表示不可用
	'''
	flag = models.CharField(max_length=1,default='1')
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	short_content = models.TextField(blank=True)
	img_content = models.TextField(blank=True)
	music_name = models.CharField(max_length=200,blank=True)
	music_songer = models.CharField(max_length=200,blank=True)
	music_title = models.CharField(max_length=200,blank=True)
	media_url = models.CharField(max_length=200,blank=True)
	closecomment = models.CharField(max_length=1,default='N')
	category = models.ForeignKey(Category,db_column='category',null=True) 
	tags = TaggableManager()
	edit_time = models.DateTimeField(auto_now=True)
	archive_date = models.CharField(max_length=10,blank=True)
	creator_id = models.IntegerField()
	creator_name = models.CharField(max_length=100)
	create_date = models.DateTimeField(auto_now=True)
	disabled = models.CharField(max_length=1,default='N')
	