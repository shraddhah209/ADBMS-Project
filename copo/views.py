#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import COadbms,PO, COatdadbms
from teachers.models import Students
from statistics import *
#from .templatetags import mathfilters
# Create your views here.



def index(request):
    s = COadbms.objects.all()
    template = loader.get_template("CO/index.html")
    context = {
        "sh": s,
    }
    return HttpResponse(template.render(context, request))


def ViewCO(request):
    html = ''
    co_no = '1'
    p = 0
    a = COatdadbms.objects.filter(cono=1)
    S = Students.objects.all()
    noofstudents = Students.objects.all().count()

    for u in a:
        for b in S:
            n = str(u.atd);
            html += '<h4>' + b.student_name + '-' + str(getattr(b, n)) + n


            '''




    context = {
       "COatd": COatd,
        "S" : S,
    }
    template = loader.get_template("copo/ViewCO.html") '''
    p = int(p/noofstudents)
    html += '<br><br> Avg of class in CO-' + str(co_no) + '  -  ' + str(p) +'%'
    return HttpResponse(html)
       # template.render(context, request))

def ViewPO(request):
    p = PO.objects.all