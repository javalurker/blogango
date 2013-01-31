from django import forms  
from django.conf import settings  
from django.utils.safestring import mark_safe  
from django.template.loader import render_to_string  
from django.utils.translation import ugettext_lazy as _  
  
class KindEditor(forms.Textarea):  
  
    def __init__(self, attrs = {}):  
        #attrs['style'] = "width:800px;height:400px;visibility:hidden;"  
        super(KindEditor, self).__init__(attrs)  
  
    def render(self, name, value, attrs=None):  
        rendered = super(KindEditor, self).render(name, value, attrs)  
        context = {  
            'name': name,  
            'MEDIA_URL':settings.STATIC_URL,  
        }  
        return  mark_safe(render_to_string('editor/kindeditor.html', context)) + rendered