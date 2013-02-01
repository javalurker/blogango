# -*- coding: utf-8 -*- 
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
import os
import time

from models import *
from config import *

def toindex(request,bloger_name,pages_id):
	title = 'd4blog'
	cur_page = int(pages_id)
	page_count = Post.objects.filter(creator_name=bloger_name,id__gt=0,disabled='N').count()
	if page_count%BLOG_PAGING_SIZE == 0 and page_count/BLOG_PAGING_SIZE > 0:
		page_count = page_count/BLOG_PAGING_SIZE+1
		pages = range(1,page_count)
	else:
		page_count = page_count/BLOG_PAGING_SIZE+1
		pages = range(1,page_count+1)
	list_posts = Post.objects.filter(creator_name=bloger_name,id__gt=0,disabled='N').order_by('-create_date')[(cur_page-1)*BLOG_PAGING_SIZE:cur_page*BLOG_PAGING_SIZE]
	archives = Archive.objects.filter(creator_name=bloger_name,disabled='N').order_by('archive_date')
	links = Link.objects.filter(creator_name=bloger_name,disabled='N').order_by('displayorder')
	category = Category.objects.filter(creator_name=bloger_name,disabled='N')
	blogerinfo = User.objects.filter(username=bloger_name)[0]
	t = get_template('index.html')
	c = RequestContext(request,locals())
	return HttpResponse(t.render(c))

def toindex_category(request,bloger_name,_category,pages_id):
	title = '%s - d4blog' % _category
	cur_page = int(pages_id)
	page_count = Post.objects.filter(creator_name=bloger_name,id__gt=0,category=_category,disabled='N').count()
	if page_count%BLOG_PAGING_SIZE == 0 and page_count/BLOG_PAGING_SIZE > 0:
		page_count = page_count/BLOG_PAGING_SIZE+1
		pages = range(1,page_count)
	else:
		page_count = page_count/BLOG_PAGING_SIZE+1
		pages = range(1,page_count+1)
	list_posts = Post.objects.filter(creator_name=bloger_name,id__gt=0,category=_category,disabled='N').order_by('-create_date')[(cur_page-1)*BLOG_PAGING_SIZE:cur_page*BLOG_PAGING_SIZE]
	archives = Archive.objects.filter(creator_name=bloger_name,disabled='N').order_by('archive_date')
	links = Link.objects.filter(creator_name=bloger_name,disabled='N').order_by('displayorder')
	category = Category.objects.filter(creator_name=bloger_name,disabled='N')
	blogerinfo = User.objects.filter(username=bloger_name)[0]
	t = get_template('index.html')
	c = RequestContext(request,locals())
	return HttpResponse(t.render(c))
	
def toindex_date(request,bloger_name,date,pages_id):
	title = '%s - d4blog' % date
	cur_page = int(pages_id)
	page_count = Post.objects.filter(creator_name=bloger_name,id__gt=0,archive_date=date,disabled='N').count()
	if page_count%BLOG_PAGING_SIZE == 0 and page_count/BLOG_PAGING_SIZE > 0:
		page_count = page_count/BLOG_PAGING_SIZE+1
		pages = range(1,page_count)
	else:
		page_count = page_count/BLOG_PAGING_SIZE+1
		pages = range(1,page_count+1)
	list_posts = Post.objects.filter(creator_name=bloger_name,id__gt=0,archive_date=date,disabled='N').order_by('-create_date')[(cur_page-1)*BLOG_PAGING_SIZE:cur_page*BLOG_PAGING_SIZE]
	archives = Archive.objects.filter(creator_name=bloger_name,disabled='N').order_by('archive_date')
	links = Link.objects.filter(creator_name=bloger_name,disabled='N').order_by('displayorder')
	category = Category.objects.filter(creator_name=bloger_name,disabled='N')
	blogerinfo = User.objects.filter(username=bloger_name)[0]
	t = get_template('index.html')
	c = RequestContext(request,locals())
	return HttpResponse(t.render(c))
	
def topostdetail(request,bloger_name,id):
	post = Post.objects.get(id=id)
	try:
		post.category
	except ObjectDoesNotExist:
		post.category = None
	archives = Archive.objects.filter(creator_name=bloger_name,disabled='N').order_by('archive_date')
	links = Link.objects.filter(creator_name=bloger_name,disabled='N').order_by('displayorder')
	category = Category.objects.filter(creator_name=bloger_name,disabled='N')
	blogerinfo = User.objects.filter(username=bloger_name)[0]
	title = '%s - d4blog' % post.title
	t = get_template('post_detail.html')
	c = RequestContext(request,locals())
	return HttpResponse(t.render(c))
	
def uploadFile(request):
	content = request.FILES.get('imgFile','')
	filename = content.name
	file_type = filename.split('.')[-1].lower()
	new_file_name = "%d.%s"% (int(time.time()), file_type)
	import sae.storage
	s = sae.storage.Client()
	ob = sae.storage.Object(content.read())
	url = s.put('fileupload', new_file_name, ob)
	sjson = {'error':0, 'url':url, 'filename':filename}
	import json
	out = json.dumps(sjson)
	return HttpResponse(out)
	
def feed_atom(request,bloger_name):
	list_posts = Post.objects.filter(creator_name=bloger_name,id__gt=0,disabled='N').order_by('-create_date')[0:BLOG_PAGING_SIZE]
	t = get_template('feed_atom.xml')
	c = RequestContext(request,locals())
	return HttpResponse(t.render(c), mimetype="text/plain")
	
def sitmap(request,bloger_name):
	posts = Post.objects.filter(creator_name=bloger_name,disabled='N').order_by('-create_date').all()
	dt = time.strftime("%Y-%m-%dT%H:%M:%S+08:00", time.localtime())
	t = get_template('sitemap.xml')
	c = RequestContext(request,locals())
	return HttpResponse(t.render(c), mimetype="text/plain")