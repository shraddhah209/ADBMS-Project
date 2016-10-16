from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^select/viewCO/$', views.ViewCO, name='viewco'),
    url(r'^po/$', views.ViewPO, name='ViewPO'),
    url(r'^addCOAtd/$',views.AddCOatd.as_view(), name='AddCOAtd'),
    url(r'^finalCO/$', views.FinalADBMS, name='finalco'),
    url(r'^selectCORange/$', views.COSelectRange, name='select'),
    url(r'^index/$', views.index, name='index'),
    ]
