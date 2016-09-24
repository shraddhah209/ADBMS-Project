from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from .models import Students
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def studentDB(request):
    json_key = 'Adbms-7c8aa9cf0720.json'
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('c:/Users/Sarbjit/Desktop/Adbms-7c8aa9cf0720.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("test").sheet1
    val = wks.acell('A1').value
    val2 = wks.acell('A2').value
    return render_to_response('teachers/studentData.html', {'value': val , 'value2': val2})


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