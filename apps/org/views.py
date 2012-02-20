from django.template.context import RequestContext
from django.shortcuts import render_to_response
from apps.models.models import Student,Parent, Teacher, School, City, School_info,Organization
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from apps.org.forms import RegisterForm, School_reg_form,City_add_form
from django.contrib.auth.models import User


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
    
def teachers_reg(request):        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():        
            dic = {
                'username':form.cleaned_data.get('username'),
                'first_name':form.cleaned_data.get('first_name'),
                'email':form.cleaned_data.get('email'),
                'is_active':True, 
                }            
            user = User( ** dic)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            teacher = Teacher(user_id = user)
            teacher.save();
            return HttpResponseRedirect(reverse('teachers_list'))
    else:
        form = RegisterForm()
    rc = RequestContext(request, {'form':form, 'title':'Registration Form'})
    return render_to_response('org/teachers_reg.html', rc,
                              context_instance=RequestContext(request)) 
    
def teacher_del(request):    
    return render_to_response('org/home.html', {},
                              context_instance=RequestContext(request))
    
def teachers_list(request):    
    rc = Teacher.objects.all()
    return render_to_response('org/teachers_list.html', rc,
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
            print info                         
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
    