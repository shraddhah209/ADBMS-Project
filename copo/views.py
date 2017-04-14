from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.template import loader
from copo.forms import SelectCOperRange
from .models import COadbms, PO, COatdadbms
from teachers.models import Students
from django.shortcuts import render
from django.db.models import Avg
import re


def index(request):
    s = COadbms.objects.all()
    template = loader.get_template("copo/index.html")
    context = {
        "sh": s
    }
    return HttpResponse(template.render(context, request))


def ViewCO(request):
    Atdmap = COatdadbms.objects.filter(cono=1)
    S = Students.objects.all()
    patterntesta = re.compile("[T][1-2]q[1-4]|[A][1-2]")
    total = []
    for b in S:
        ta = 0
        texp = 0
        pta = 0
        pexp = 0
        for u in Atdmap:
            n = str(u.atd)
            m = getattr(b, n)
            if patterntesta.match(n):
                ta += 1
                pta += int(m)
            else:
                texp += 1
                pexp += int(m)
        ttl = (((pta * 100)/(5 * ta)) + ((pexp * 100)/(10 * texp))) / 2
        total.append(ttl)
    context = {
        "S": S,
        "a": Atdmap,
        "total": total,
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
    html = "<!DOCTYPE html>\
<html >\
<head>\
    <meta charset='UTF-8'>\
    <title></title>\
    <link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>\
    <link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css'>\
    <script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>\
    <script src='http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>\
	<script>\
	$(function() {\
        $('#nav li a').click(function() {\
           $('#nav li').removeClass();\
           $($(this).attr('href')).addClass('active');\
        });\
     });\
</script>\
<style> th, td {\
    padding: 15px;\
    text-align: left;\
    font-family: TimesNewRoman;\
    font-size: 20px;\
}</style></head>\
<body>\
    		<div class='wrapper'>\
    			<div class='container'>\
    				<nav role='navigation' class='navbar navbar-inverse navbar-embossed navbar-lg navbar-fixed-top'>\
    					<div class='container'>\
    						<div class='navbar-header'>\
    							<button data-target='#navbar-collapse-02' data-toggle='collapse' class='navbar-toggle' type='button'>\
    								<span class='sr-only'>Toggle navigation</span>\
    							</button>\
    							<a href='/teachers/subject' class='navbar-brand brand'> PROFE </a>\
   							</div>\
    						<div id='navbar-collapse-02' class='collapse navbar-collapse'>\
    							<ul class='nav navbar-nav' id='nav'>\
    								<li ><a href='/copo/po'>VIEW POS</a></li>\
									<li ><a href='/copo/index/'>VIEW COS</a></li>\
									<li ><a href='/copo/addCOAtd'>MAP CO</a></li>\
									<li ><a href='/copo/finalCO'>ATTAINMENT OF CO</a></li>\
									<li ><a href='/copo/mapCOPO'>ATTAINMENT OF PO</a></li>\
									<li ><a href='/copo/selectCORange/'>EACH STUDENTS ATTAINMENT</a></li>\
									<li class='active '><a href='/teachers/studentDB'>STUDENT DB</a></li>\
                                </ul>\
    							<ul class='nav navbar-nav navbar-right'>\
    								<li class='propClone'>\
    									<a href='{% url 'teachers:login' %}'>LOG OUT <span class='fa fa-lock'></span></a>\
    								</li>\
    							</ul>\
    						</div><!-- /.navbar-collapse -->\
    					</div><!-- /.container -->\
    				</nav>\
    				<!-- /.row -->\
    			</div><!-- /.container -->\
    		</div><!-- /.wrapper -->\
<br><br><br> <br><br>\
</body><div  style='margin-left: 30px;'>\
<CENTER><h4>Attainment of Course Outcomes:</h4><br><br><table border =2><tr><th rowspan=2 >Course Outcome</th><th colspan=3 >University Examination</th><th colspan=6 >Direct Method</th><th rowspan=2>Indirect method</th>\
        </tr><tr><th>ESE</th><th>VIVA/PR</th><th>Avg</th><th>Term test 1</th><th>Term test 2\
        </th><th>Assignment</th><th>Lab</th><th>Internal Assessment Average</th><th>Direct Avg</th></tr>"
    c = 1
    Atdmap1 = COatdadbms.objects.all()
    S = Students.objects.all()
    sem = Students.objects.all().aggregate(Avg('final_marks'))
    for key, value in sem.items():
        semmarks = value
    semmarks = int(semmarks)
    semmarks = round((semmarks*100/80), 2)
    v = Students.objects.all().aggregate(Avg('viva'))
    for key, value in v.items():
        viva = value
    viva = int(viva)
    viva = round((viva*100/25), 2)
    avg = round(((viva + semmarks)/2), 2)
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
        davg = round(((avg +ptotal)/2), 2)
        if c == 1:
            html += "<tr><td>CO " + str(c) + "</td><td rowspan=5 >" + str(semmarks)+ "</td><td rowspan=5 >" + str(viva)+\
                    "</td><td rowspan=5 >" + str(avg)+"</td><td>" +\
                    str(pt1) + "</td><td>" + str(pt2) + "</td><td>" + str(pa) + "</td><td>" + str(pexp) + \
                    "</td><td>" + str(ptotal)+"</td><td>" +str(davg) + "</td><td> - </td></tr>"
        else:
            html += "<tr><td>CO " + str(c) + "</td><td>" + str(pt1) + "</td><td>" + str(pt2) + "</td><td>" + str(
                pa) + "</td><td>" + str(pexp) + "</td><td>" + str(ptotal) + "</td><td>" +str(davg) +\
                    "</td><td> - </td></tr>"
        c += 1
    html += "</table></div>"
    return HttpResponse(html)

def COSelectRange(request):
    form_class = SelectCOperRange
    co = COadbms.objects.all()
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            rmin = request.POST.get(
                'rangemin'
                , '')
            rmax = request.POST.get(
                'rangemax'
                , '')
            selected_co = request.POST.get('co')
            selected_co = int(selected_co)
            Atdmap = COatdadbms.objects.filter(cono=selected_co)
            coobj = COadbms.objects.filter(co_no=selected_co)
            S = Students.objects.all()
            patterntesta = re.compile("[T][1-2]q[1-4]|[A][1-2]")
            total = []
            rollno = []
            for b in S:
                ta = 0
                texp = 0
                pta = 0
                pexp = 0
                for u in Atdmap:
                    n = str(u.atd)
                    m = getattr(b, n)
                    if patterntesta.match(n):
                        ta += 1
                        pta += int(m)
                    else:
                        texp += 1
                        pexp += int(m)
                if ta!=0 and texp!=0:
                    ttl = int((((pta * 100) / (5 * ta)) + ((pexp * 100) / (10 * texp))) / 2)
                elif texp!=0:
                    ttl = int((pexp * 100) / (10 * texp))
                else:
                    ttl = int((pta * 100) / (5 * ta))
                rmin = int(rmin)
                rmax = int(rmax)
                if ttl >= rmin and ttl <= rmax:
                    rollno.append(b.student_roll)
                    total.append(ttl)

        context = {
                    'rmin': rmin, 'rmax': rmax, 'total': total, 'S': S, 'Atdmap': Atdmap,
                    'rollno': rollno, 'co':selected_co, 'coobj':coobj
        }
        template = loader.get_template("copo/ViewCORange.html")
        return HttpResponse(template.render(context, request))
    return render(request, 'copo/Selection.html', {'form': form_class, 'co':co})


def mapCOPO(request):
    c = 1
    Atdmap1 = COatdadbms.objects.all()
    S = Students.objects.all()
    sem = Students.objects.all().aggregate(Avg('final_marks'))
    for key, value in sem.items():
        semmarks = value
    semmarks = int(semmarks)
    semmarks = round((semmarks * 100 / 80), 2)
    v = Students.objects.all().aggregate(Avg('viva'))
    for key, value in v.items():
        viva = value
    viva = int(viva)
    viva = round((viva * 100 / 25), 2)
    avg = round(((viva + semmarks) / 2), 2)
    noofstudents = Students.objects.all().count()
    patterntest1 = re.compile("^([T][1][q][1-4]+)+$")
    patterntest2 = re.compile("^([T][2][q][1-4]+)+$")
    patternass = re.compile("^([A][1-2]+)+$")
    patternexp = re.compile("^([E][x][p][1,2,3,4,5,6,7,8,9,10]+)+$")
    po1 = 0
    po2 = 0
    po3 = 0
    po4 = 0
    po5 = 0
    po6 = 0
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    while c <= 5:
        k = 0
        pt1 = 0
        pt2 = 0
        pa = 0
        pexp = 0
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
        davg = round(((avg + ptotal) / 2), 2)



        copo = COadbms.objects.filter(co_no=str(c))
        for po in copo:
            #html = str(po.po1)+"-"+str(po.po2)+"-"+str(po.po3)+"-"+str(po.po4)+"-"+str(po.po5)+"-"+str(po.po6)+"-"
            if po.po1 == '1':
                po1 = po1 + davg
                p1 += 1
            if po.po2 == '1':
                po2 = po2 + davg
                p2 += 1
            if po.po3 == '1':
                po3 = po3 + davg
                p3 += 1
            if po.po4 == '1':
                po4 = po4 + davg
                p4 += 1
            if po.po5 == '1':
                po5 = po5 + davg
                p5 += 1
            if po.po6 == '1':
                po6 = po6 + davg
                p6 += 1
        c += 1

    po1 = round(po1/p1,2)
    po2 = round(po2/p2,2)
    po3 = round(po3/p3,2)
    po4 = round(po4/p4,2)
    po5 = round(po5/p5,2)
    po6 = round(po6/p6,2)
    po = PO.objects.all()
    context = {
        'po1':po1,'po2':po2,'po3':po3,'po4':po4,'po5':po5,'po6':po6, 'po':po
    }
    template = loader.get_template("copo/mapCOPO.html")
    return HttpResponse(template.render(context, request))
    #html = str(p1)+"--"+str(p2)+"--"+str(p3)+"--"+str(p4)+"--"+str(p5)+"--"+str(p6)+"--"+str(po1)+"--"+str(po2)+"--"+str(po3)+"--"+str(po4)+"--"+str(po5)+"--"+str(po6)+"--"
    #return HttpResponse(html)





