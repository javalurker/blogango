blogango
========
blogango是一个基于django框架的python博客程序

基于：
django1.4

django admin site

django-taggit

jingo

多说评论系统

1、修改settings.py配置如下：
A、加入jingo
TEMPLATE_LOADERS = (
  'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
B、修改INSTALLED_APPS
	...

	'blogango',
	...

2、创建多说评论系统账号，修改macros.html
<!-- Duoshuo Comment BEGIN -->
<div class="ds-thread" data-thread-key="0" data-title="{{ title }}"></div>
<script type="text/javascript">
var duoshuoQuery = {short_name:"d4blog"};
</script>
<script type="text/javascript" src="http://static.duoshuo.com/embed.js" async="true"></script>
<!-- Duoshuo Comment END -->
改成你自己的多说账号


3、执行：python manage.py syncdb
创建你的admin site账号，
4、启动服务，输入http://localhost:8000/blog/javalurker（其中javalurker为你的系统账号，admin创建；blog为你自定义的urls）
