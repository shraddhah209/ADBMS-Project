#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import COadbms,PO, COatdadbms
from teachers.models import Students


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
    Atdmap = COatdadbms.objects.filter(cono=1)
    S = Students.objects.all()
    noofstudents = Students.objects.all().count()

    for u in Atdmap:
        for b in S:
            n = str(u.atd)
            m = getattr(b, n)
            p += int(m)
    p = int(p / noofstudents)
    context = {
        "S": S,
        "a": Atdmap,
        "p": p,
    }
    template = loader.get_template("copo/ViewCO.html")

    return HttpResponse(template.render(context, request))

def ViewPO(request):
    p = PO.objects.all





