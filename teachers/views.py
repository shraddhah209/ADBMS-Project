from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404,render, redirect
from django.template import loader
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.template import RequestContext
from django.views import generic
from django import forms
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Students
from .forms import UserForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def studentDB(request):
    json_key = 'Adbms-7c8aa9cf0720.json'
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('c:/Users/Sarbjit/Desktop/Adbms-7c8aa9cf0720.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("test").sheet1
    student_list = ["student_roll","student_name","Exp1"]
    blah = Students.objects.all()
    count = len(blah)
    return render(request,'teachers/studentData.html', {'wks':count})

def save(request):
    json_key = 'Adbms-7c8aa9cf0720.json'
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('c:/Users/Sarbjit/Desktop/Adbms-7c8aa9cf0720.json',scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("test").sheet1
    count = wks.rows_count
    c = 2
    while c<=count:
        all_students = Students.objects.filter(pk=c-1)
        for a in all_students:
            a.student_roll != wks.acell('A' + str(c)).value
            a.student_name = wks.acell('B'+ str(c)).value
            a.Exp1 = wks.acell('C' + str(c)).value
            a.Exp2 = wks.acell('D' + str(c)).value
            a.Exp3 = wks.acell('E' + str(c)).value
            a.Exp4 = wks.acell('F' + str(c)).value
            a.Exp5 = wks.acell('G' + str(c)).value
            a.Exp6 = wks.acell('H' + str(c)).value
            a.Exp7 = wks.acell('I' + str(c)).value
            a.Exp8 = wks.acell('J' + str(c)).value
            a.Exp9 = wks.acell('K' + str(c)).value
            a.Exp10 = wks.acell('L' + str(c)).value
            a.exp_avg = wks.acell('M' + str(c)).value
            a.T1q1 = wks.acell('N' + str(c)).value
            a.T1q2 = wks.acell('O' + str(c)).value
            a.T1q3 = wks.acell('P' + str(c)).value
            a.T1q4 = wks.acell('Q' + str(c)).value
            a.T1_total = wks.acell('R' + str(c)).value
            a.T2q1 = wks.acell('S' + str(c)).value
            a.T2q2 = wks.acell('T' + str(c)).value
            a.T2q3 = wks.acell('U' + str(c)).value
            a.T2q4 = wks.acell('V' + str(c)).value
            a.T2_total = wks.acell('W' + str(c)).value
            a.TT_avg = wks.acell('X' + str(c)).value
            a.A1 = wks.acell('Y' + str(c)).value
            a.A2 = wks.acell('Z' + str(c)).value
            a.Ass_avg = wks.acell('AA' + str(c)).value
            a.attendance = wks.acell('AB' + str(c)).value
            a.final_marks = wks.acell('AC' + str(c)).value
        c += 1
        a.save()

    return render_to_response('teachers/bullshit.html',{'val':a.student_name})

def stud(request):
    all_students = Students.objects.all()
  ##  html = ""
  ##     html += str(blah.T1q1)+"      "
  ##    return HttpResponse(html)
    template = loader.get_template("teachers/studentData.html")
    context = {
        "all_stud": all_students,
    }
    return HttpResponse(template.render(context,request))

def detail(request, student_roll):
    return HttpResponse("roll no is : "+str(student_roll)+"       name is : ")

class UserFormView(View):
    form_class = UserForm
    template_name='teachers/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            email=request.POST.get('email','')
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            #email=form.cleaned_data['email']
            # to change users password
            user.set_password(password)
            user.save()

            user = auth.authenticate(username=username, password=password, email=email)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('teachers: studentDB')

        return render(request, self.template_name, {'form': form})




