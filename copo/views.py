#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import COadbms,PO
# Create your views here.


def index(request):
    s = COadbms.objects.all()
    template = loader.get_template("CO/index.html")
    context = {
        "sh": s,
    }
    return HttpResponse(template.render(context, request))


