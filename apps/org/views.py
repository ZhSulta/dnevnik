from django.template.context import RequestContext
from django.shortcuts import render_to_response
from apps.models.models import Student,Parent, Teacher, School, City, School_info,Organization,Temporary
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from apps.org.forms import RegisterForm, School_reg_form,City_add_form,TemporaryForm
from django.contrib.auth.models import User
from dnevniktools.dbutils import get_nextautoincrement
from apps.models import settings as ns
from random import random


def index(request):    
    return render_to_response('org/home.html', {},
                              context_instance=RequestContext(request))

def students_reg(request):          
    return render_to_response('org/students_reg.html', {},
                              context_instance=RequestContext(request))
    
def student_del(request):        
    return render_to_response('org/home.html', {},
                              context_instance=RequestContext(request))
    
def students_info(request):        
    return render_to_response('org/home.html', {},
                              context_instance=RequestContext(request))
    
def students_list(request):    
    rc = Student.objects.all()
    return render_to_response('org/students_list.html', rc,
                              context_instance=RequestContext(request))
    
def parents_reg(request):
    return render_to_response('org/parents_reg.html', {},
                              context_instance=RequestContext(request))
        
def parents_del(request):    
    return render_to_response('org/home.html', {},
                              context_instance=RequestContext(request))
    
def parents_info(request):    
    return render_to_response('org/home.html', {},
                              context_instance=RequestContext(request))
    
def parents_list(request):    
    rc = Parent.objects.all()
    return render_to_response('org/parents_list.html', rc,
                              context_instance=RequestContext(request))
def rand():
    r = random()
    cur = long(r*100000000000)
    if cur < 10000000000:
        cur = cur * 10000000000
    print cur    
    pwd1 = ''
    index = 0 
    while index<5:
        c1 = cur%62
        if c1< 10:
            pwd1 = pwd1 + str(c1)
        elif c1>=10 and c1<36:
            d = c1 - 10
            pwd1 = pwd1 + chr((ord('a')+d))
        else:
            d = c1 - 36
            pwd1 = pwd1 + chr((ord('A')+d))
        cur = cur/62
        index = index+1
    return pwd1

def teachers_temp_reg(request):
    
    if request.method == 'POST':
        form = TemporaryForm(request.POST)
        if form.is_valid():                                
            number1  = form.cleaned_data['number']
            school1 = form.cleaned_data['school']
            city1 = form.cleaned_data['city']
            i = 1            
            while i <= number1: 
                pwd1 = rand()
                username1 = rand()                               
                temporary = Temporary(school = school1, city = city1, role = ns.TEACHER_POSITION,username = username1, pwd = pwd1)
                temporary.save()
                print i                
                i = i+1
            return HttpResponseRedirect(reverse('teachers_list'))
    else:
        form = TemporaryForm()
    rc = RequestContext(request, {'form':form, 'title':'Registration Form'})
    return render_to_response('org/teachers_reg.html', rc,
                              context_instance=RequestContext(request)) 

def teacher_del(request,id):    
    teacher_temp = Temporary.objects.get(pk = id)
    teacher_temp.delete()
    teacher = Teacher.objects.all()
    temp = Temporary.objects.all()
    return render_to_response('org/teachers_list.html', {'teacher':teacher,'temp':temp},
                              context_instance=RequestContext(request))
    
def teacher_temp_del(request,id):    
    teacher_temp = Temporary.objects.get(pk = id)
    teacher_temp.delete()
    teacher = Teacher.objects.all()
    temp = Temporary.objects.all()
    return render_to_response('org/teachers_list.html', {'teacher':teacher,'temp':temp},
                              context_instance=RequestContext(request))
        
def teachers_list(request):    
    teacher = Teacher.objects.all()
    temp = Temporary.objects.all()    
    return render_to_response('org/teachers_list.html', {'teacher':teacher,'temp':temp},
                              context_instance=RequestContext(request))
    
def teachers_info(request):    
    return render_to_response('org/home.html', {},
                              context_instance=RequestContext(request))
    
def school_reg(request):
    org = Organization.objects.get(name = 'katev')
    if request.method == 'POST':
        form = School_reg_form(request.POST)
        if form.is_valid():                                
            info = form.save()                                               
            school_info = School_info(school = info)   
            school_info.save()
            return HttpResponseRedirect(reverse('schools_list'))
    else:
        form = School_reg_form()
    rc = RequestContext(request, {'form':form, 'org':org,'title':'School Registration Form'})    
    return render_to_response('org/school_reg.html', rc,
                              context_instance=RequestContext(request)) 
    
def school_del(request, id):    
    school = School.objects.get(pk = id)
    school.delete()    
    rc = School.objects.all()
    return render_to_response('org/schools_list.html', {'rc':rc},
                              context_instance=RequestContext(request))
        
def schools_list(request):    
    rc = School.objects.all()
    return render_to_response('org/schools_list.html', {'rc':rc},
                              context_instance=RequestContext(request))
    
def school_info(request, id):
    rc = School_info.objects.get(pk = id)    
    return render_to_response('org/school_info.html', {'rc':rc},
                              context_instance=RequestContext(request))
    
def city_add(request):  
    if request.method == 'POST':
        form = City_add_form(request.POST)
        if form.is_valid():        
            form.save()                                            
            return HttpResponseRedirect(reverse('city_list'))
    else:
        form = City_add_form()
    rc = RequestContext(request, {'form':form, 'title':'Add City Form'})    
    return render_to_response('org/city_add.html', rc,
                              context_instance=RequestContext(request))
    
def city_list(request):  
    rc = City.objects.all()    
    return render_to_response('org/city_list.html', {'rc':rc},
                              context_instance=RequestContext(request))
    
def city_del(request, id):
    city = City.objects.get(pk = id)
    city.delete()

    rc = City.objects.all()
    return render_to_response('org/city_list.html', {'rc':rc},
                              context_instance=RequestContext(request))
    
    