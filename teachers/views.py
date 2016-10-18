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
    blah = Students.objects.all()
    count = len(blah)
    c = 1
    cell_list = wks.range('B2:AC2')

    for cell in cell_list:
        s = Students.objects.filter(pk=c)
        for a in s:
            wks.update_cell(c + 1, 1, a.student_roll)
            wks.update_cell(c + 1, 2, a.student_name)
            wks.update_cell(c + 1, 3, a.Exp1)
            wks.update_cell(c + 1, 4, a.Exp2)
            wks.update_cell(c + 1, 5, a.Exp3)
            wks.update_cell(c + 1, 6, a.Exp4)
            wks.update_cell(c + 1, 7, a.Exp5)
            wks.update_cell(c + 1, 8, a.Exp6)
            wks.update_cell(c + 1, 9, a.Exp7)
            wks.update_cell(c + 1, 10, a.Exp8)
            wks.update_cell(c + 1, 11, a.Exp9)
            wks.update_cell(c + 1, 12, a.Exp10)
            #wks.update_cell(c + 1, 13, a.exp_avg)
            wks.update_cell(c + 1, 14, a.T1q1)
            wks.update_cell(c + 1, 15, a.T1q2)
            wks.update_cell(c + 1, 16, a.T1q3)
            wks.update_cell(c + 1, 17, a.T1q4)
            #wks.update_cell(c + 1, 18, a.T1_total)
            wks.update_cell(c + 1, 19, a.T2q1)
            wks.update_cell(c + 1, 20, a.T2q2)
            wks.update_cell(c + 1, 21, a.T2q3)
            wks.update_cell(c + 1, 22, a.T2q4)
            # wks.update_cell(c + 1, 23, a.T2_total)
            #wks.update_cell(c + 1, 24, a.TT_avg)
            wks.update_cell(c + 1, 25, a.A1)
            wks.update_cell(c + 1, 26, a.A2)
            # wks.update_cell(c + 1, 27, a.Ass_avg)
            wks.update_cell(c + 1, 28, a.attendance)
            wks.update_cell(c + 1, 29, a.final_marks)
        c += 1
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




