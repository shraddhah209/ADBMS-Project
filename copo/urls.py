from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ViewCO, name='index'),
    url(r'^po/$', views.ViewPO, name='ViewPO'),
    url(r'^editCOAtd/$',views.AddCOatd.as_view(), name='AddCOAtd'),
    url(r'^editCOAtd/copo/$', views.ViewCO, name='index'),
    url(r'^finalCO/$', views.FinalADBMS, name='index'),
]


