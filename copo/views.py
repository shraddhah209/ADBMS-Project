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
    S = Students.objects.all()
    noofstudents = Students.objects.all().count()
    if co_no == '1':
        for b in S:
            n = (int(b.T1q1)+int(b.T1q2)+int(b.T1q3)+int(b.A1))*100/20
            m = (int(b.Exp1) + int(b.Exp2)+ int(b.Exp3)+ int(b.Exp4))*10/4
            p += mean([n, m])
            html += '<h4>' + b.student_name + '-' + str(b.T1q2) + '-' + str(b.T1q2) + '-' + str(b.T1q3) + '-' + str(b.A1) + '-' + str(b.Exp1) + '-' + str(b.Exp2) + '-' + str(b.Exp3) + '-' + str(b.Exp4) + '-' + str(mean([n, m])) + '</h4><br>'
    elif co_no == '2':
        for b in S:
            m = (int(b.Exp3) + int(b.Exp4) + int(b.Exp9)) * 100 / 30
            html += '<h4>' + b.student_name + '-' + str(b.Exp3) + '-' + str(b.Exp4) + '-' + str(b.Exp5) + '-' + str(m) + '</h4><br>'
    elif co_no == '3':
        for b in S:
            n = (int(b.A2)) * 20
            m = (int(b.Exp6)+int(b.Exp10)) * 5
            html += '<h4>' + b.student_name + '-' + str(b.A2) + '-' + str(b.Exp6) + '-' + str(b.Exp10) + '-' + str(
                mean([n, m])) + '</h4><br>'
    elif co_no == '4':
        for b in S:
            n = (int(b.T2q3) + int(b.T2q4))*10
            m = (int(b.Exp5)+int(b.Exp7))*5
            html += '<h4>' + b.student_name + '-' + str(b.T2q3) + '-' + str(b.T2q4) + str(b.Exp5) + '-' +\
                    str(b.Exp7) + '-' + str(mean([n, m])) + '</h4><br>'
    elif co_no == '5':
        for b in S:
            n = (int(b.T2q1) + int(b.T2q2)+int(b.Exp8)) * 10
            html += '<h4>' + b.student_name + '-' + str(b.T2q1) + '-' + str(b.T2q2) + str(b.Exp8) + '-' + str(n)\
                + '</h4><br>'
    #context = {
     #  "COatd": COatd,
      #  "S" : S,
    #}
    #template = loader.get_template("copo/ViewCO.html")
    p = int(p/noofstudents)
    html += '<br><br> Avg of class in CO-' + str(co_no) + '  -  ' + str(p) +'%'
    return HttpResponse(html)
       # template.render(context, request))