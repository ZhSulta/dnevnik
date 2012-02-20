from django.shortcuts import render_to_response
from django.template.context import RequestContext
from registration.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def student_main(request,student_id):    
    c = {'id':student_id}
    return render_to_response('student/main.html', c,
                              context_instance=RequestContext(request))
    
def student_profile(request,student_id):
    d = {'id':student_id}
    return render_to_response('student/profile.html', d,
                              context_instance=RequestContext(request))


