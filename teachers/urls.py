from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.studentDB, name='studentDB'),
    url(r'^(?P<student_roll>[0-9]+)/$', views.detail, name='detail'),

]