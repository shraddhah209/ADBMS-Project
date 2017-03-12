from django.conf.urls import include,url
from django.contrib import admin
#urls main
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^teachers/', include("teachers.urls")),
    url(r'^copo/', include("copo.urls")),

]
