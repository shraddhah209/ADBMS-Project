from django.http import HttpResponse
from django.template import loader
from .models import Students


def studentDB(request):
    all_students = Students.objects.all()
    template = loader.get_template("teachers/studentData.html")
    context = {
        "all_stud": all_students,
    }
    return HttpResponse(template.render(context,request))


def detail(request, student_roll):
    return HttpResponse("roll no is : "+str(student_roll)+"       name is : ")