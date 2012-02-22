from accounts.forms import LoginForm
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from apps.models.models import Temporary

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username1  = form.cleaned_data['username']
            pwd1  = form.cleaned_data['pwd']
            temp = Temporary.objects.get(username = username1,pwd = pwd1)            
    else:
        form = LoginForm()
    rc = RequestContext(request, {'form':form, 'title':'Registration Form'})
    return render_to_response('registration/login.html', rc,
                              context_instance=RequestContext(request))     

#def logout(request):
#    _logout(request)
#    return HttpResponseRedirect(reverse('login'))

            