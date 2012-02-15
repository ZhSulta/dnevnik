from django.shortcuts import render_to_response
from registration.forms import RegistrationForm
from dnevniktools.dbutils import get_nextautoincrement
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def school_reg(request):
    return render_to_response('accounts/school_reg.html',{})

def parents_reg(request):
    return render_to_response('accounts/parents_reg.html',{})

def teachers_reg(request):
    return render_to_response('accounts/teachers_reg.html',{})

def students_reg(request):
    return render_to_response('accounts/students_reg.html',{})


def quick_register(request, template = "registration/registration_form.html", send_email = True, extra_context = None):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        next_id = get_nextautoincrement(User)
        if form.is_valid():
            dic = {
                'email':form.cleaned_data.get('email'),
                'is_active':True,
                }
            user = User(** dic)
            user.username = "user%05d" % next_id
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            if send_email:
                from django.core.mail import send_mail
                current_site = Site.objects.get_current()

                subject = render_to_string('registration/email_subject.txt',
                                           { 'site': current_site })
                # Email subject *must not* contain newlines
                subject = ''.join(subject.splitlines())

                message = render_to_string('registration/email.txt',
                                           {'site': current_site })

                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

            new_user = authenticate(username = request.POST['email'],
                                    password = request.POST['password1'])
            login(request, new_user)

            next_page = request.REQUEST.get('next', '/cart/')
            return HttpResponseRedirect(next_page)

    form = RegistrationForm()
    return HttpResponseRedirect(reverse('register'))