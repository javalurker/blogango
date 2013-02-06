blogango
========
blogango is blog app,base django framework with python.

# requirements：  
> django1.4  
> django admin site  
> django-taggit  
> jinja2  
> jingo  
> duoshuo. a social comment system  

# step by step  
## 1、install jinja2，  
> easy_install jinja2  

## 2、update settings.py：

### A、add jingo,update settings.py

> TEMPLATE_LOADERS = (  
>     'jingo.Loader',  
>     'django.template.loaders.filesystem.Loader',  
>     'django.template.loaders.app_directories.Loader',  
> )


### B、add django-taggit


### C、update INSTALLED_APPS:

> ...  
> 'blogango',  
> 'taggit',  
> ...
	

## 3、you must create duoshuo comment system account，update macros.html

> <!-- Duoshuo Comment BEGIN -->  
> <div class="ds-thread" data-thread-key="0" data-title="{{ title }}"></div>  
> <script type="text/javascript">  
> var duoshuoQuery = {short_name:"d4blog"};  
> </script>  
> <script type="text/javascript" src="http://static.duoshuo.com/embed.js" async="true"></script>  
> <!-- Duoshuo Comment END -->

update your username


## 4、python manage.py syncdb


## 5、run server，

input http://localhost:8000/blog/javalurker in your browser (javalurker is your admin site username；blog is your urls config)
