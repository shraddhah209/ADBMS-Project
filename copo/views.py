#from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.template import loader
from .models import COadbms,PO, COatdadbms
from teachers.models import Students
import re

def index(request):
    s = COadbms.objects.all()
    template = loader.get_template("CO/index.html")
    context = {
        "sh": s,
    }
    return HttpResponse(template.render(context, request))


def ViewCO(request):
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
    p = PO.objects.all()
    template = loader.get_template("copo/ViewPO.html")
    context = {
        "p": p,
    }
    return HttpResponse(template.render(context, request))


class AddCOatd(CreateView):
    model = COatdadbms
    fields = ['cono', 'atd']

def FinalADBMS(request):
    html = ""
    c = 1
    ptotal = 0
    Atdmap1 = COatdadbms.objects.all()
    S = Students.objects.all()
    noofstudents = Students.objects.all().count()
    patterntest1 = re.compile("^([T][1][q][1-4]+)+$")
    patterntest2 = re.compile("^([T][2][q][1-4]+)+$")
    patternass = re.compile("^([A][1-2]+)+$")
    patternexp = re.compile("^([E][x][p][1,2,3,4,5,6,7,8,9,10]+)+$")
    while c <= 5:
        pt1 = 0
        pt2 = 0
        pa = 0
        pexp = 0
        ptotal = 0
        t1 = 0
        t2 = 0
        exp = 0
        ass = 0
        for u in Atdmap1:
            if int(u.cono) == c:
                n = str(u.atd)
                if patterntest1.match(n):
                    t1 += 1
                    for b in S:
                        m = getattr(b, n)
                        pt1 += int(m)
                if patterntest2.match(n):
                    t2 += 1
                    for b in S:
                        m = getattr(b, n)
                        pt2 += int(m)
                if patternass.match(n):
                    ass += 1
                    for b in S:
                        m = getattr(b, n)
                        pa += int(m)
                if patternexp.match(n):
                    exp += 1
                    for b in S:
                        m = getattr(b, n)
                        pexp += int(m)
        if t1:
            pt1 = int(pt1 * 100 / (noofstudents * 5 * t1))
        if t2:
            pt2 = int(pt2 * 100 / (noofstudents * 5 * t2))
        if ass:
            pa = int(pa * 100 / (noofstudents * 5 * ass))
        if exp:
            pexp = int(pexp * 100 / (noofstudents * 10 * exp))
        ptotal = int(pt1 + pt2 + pa + pexp) / 4
        html += str(c) + "t1   " + str(pt1) + "  t2    " + str(pt2) + "  Ass   " + str(pa) + "  Exp   " + str(pexp) + "  Total   " + str(ptotal)+"<br>"
        c += 1
    return HttpResponse(html)















