from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView
from views import *
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', home, {}, name="home"),
    (r'^login/$', login_user, {}, 'user_login'),
    (r'^logout/$', logout_user, {}, 'user_logout'),
    (r'^get/clases/$', get_clases_json, {}, 'get_clases_json'),
    (r'^update/clase/$', update_clase_json, {}, 'update_clase_json'),
    (r'^administrador/$', administrador, {}, 'administrador'),  
    (r'^alumnos/clase/(?P<clase_id>\d+)/$', alumnos_clase, {}, 'alumnos_clase'),  
    (r'^guardar/alumno/(?P<alumno_id>\d+)/clase/(?P<clase_id>\d+)/$', guardar_alumno, {}, 'guardar_alumno'),  
    (r'^borrar/alumno/(?P<alumno_id>\d+)/$', borrar_alumno, {}, 'borrar_alumno'),  
    (r'^tabla/alumnos/clase/(?P<clase_id>\d+)/$', tabla_alumnos, {}, 'tabla_alumnos'),  
    (r'^admin/', include(admin.site.urls)),    
      
)