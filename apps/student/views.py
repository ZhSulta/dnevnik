from django.shortcuts import render_to_response
from django.template.context import RequestContext
from registration.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def student_main(request,student_id):    
    return render_to_response('student/main.html', {'id':student_id},
                              context_instance=RequestContext(request))
    
def student_profile(request,student_id):
    return render_to_response('student/profile.html', {'id':student_id},
                              context_instance=RequestContext(request))


