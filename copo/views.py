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
    context = {
        "S": S,
        "a": Atdmap,
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
    html = "<table border =2><tr><th>CO</th><th>Term test 1</th><th>Term test 2\
        </th><th>Assignment</th><th>Experiment</th><th>Total</th></tr>"
    c = 1
    Atdmap1 = COatdadbms.objects.all()
    S = Students.objects.all()
    noofstudents = Students.objects.all().count()
    patterntest1 = re.compile("^([T][1][q][1-4]+)+$")
    patterntest2 = re.compile("^([T][2][q][1-4]+)+$")
    patternass = re.compile("^([A][1-2]+)+$")
    patternexp = re.compile("^([E][x][p][1,2,3,4,5,6,7,8,9,10]+)+$")
    while c <= 5:
        k = 0
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
                        if m != 0:
                            pt1 += int(m)
                        else:
                            t1 -= 1
                            break
                if patterntest2.match(n):
                    t2 += 1
                    for b in S:
                        m = getattr(b, n)
                        if m != 0:
                            pt2 += int(m)
                        else:
                            t2 -= 1
                            break
                if patternass.match(n):
                    ass += 1
                    for b in S:
                        m = getattr(b, n)
                        if m != 0:
                            pa += int(m)
                        else:
                            ass -= 1
                            break
                if patternexp.match(n):
                    exp += 1
                    for b in S:
                        m = getattr(b, n)
                        if m != 0:
                            pexp += int(m)
                        else:
                            exp -= 1
                            break
        if t1:
            k += 1
            pt1 = round(pt1 * 100 / (noofstudents * 5 * t1), 2)
        if t2:
            k += 1
            pt2 = round(pt2 * 100 / (noofstudents * 5 * t2), 2)
        if ass:
            k += 1
            pa = round(pa * 100 / (noofstudents * 5 * ass), 2)
        if exp:
            k += 1
            pexp = round(pexp * 100 / (noofstudents * 10 * exp), 2)
        ptotal = round((pt1 + pt2 + pa + pexp) / k, 2)
        html += "<tr><td>" + str(c) + "</td><td>" + str(pt1) + "</td><td>" + str(pt2) + "</td><td>" + str(pa) + "</td><td>" + str(pexp) + "</td><td>" + str(ptotal)+"</td></tr>"
        c += 1
    html += "</table>"
    return HttpResponse(html)















