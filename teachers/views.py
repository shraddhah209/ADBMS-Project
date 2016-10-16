from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
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
    all_students = Students.objects.all()
    count = len(all_students)
    blah = wks.col_values(2)
    stud = Students(pk=(count+1))
    stud.student_name = blah
    stud.save()
    return render_to_response('teachers/studentData.html', {'wks':count})

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




