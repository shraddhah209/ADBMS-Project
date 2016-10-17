from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'teachers'
urlpatterns = [
    url(r'^studentDB$', views.studentDB, name='studentDB'),
    url(r'^(?P<student_roll>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login/$', views.UserFormView.as_view(), name='login'),
    url(r'^save$', views.save, name='save')
   # url(r'^bullshit$', views.bullshit, name='bullshit')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
