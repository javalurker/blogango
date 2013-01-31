from django.conf.urls import patterns, include, url
from views import toindex,toindex_category,toindex_date,feed_atom,topostdetail,sitmap,uploadFile

urlpatterns = patterns('',
    url(r'^(?P<bloger_name>\w+)/$', toindex, {'pages_id':1}),
    url(r'^(?P<bloger_name>\w+)/p/(?P<pages_id>\w+)/$', toindex, name='toindex'),
    url(r'^(?P<bloger_name>\w+)/t/(?P<_category>\S+)/(?P<pages_id>\w+)/$', toindex_category),
    url(r'^(?P<bloger_name>\w+)/date/(?P<date>\w+)/(?P<pages_id>\w+)/$', toindex_date),
    url(r'^(?P<bloger_name>\w+)/a/(?P<id>\w+)/$', topostdetail),
    url(r'^(?P<bloger_name>\w+)/feed/$', feed_atom),
    url(r'^(?P<bloger_name>\w+)/sitmap/$', sitmap),
    url(r'^upload/uploadFile/$', uploadFile),
)