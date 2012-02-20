
#def login(request):
#    if request.method == 'POST':
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            cd = form.cleaned_data
#            user = authenticate(username=cd.get('username'), password=cd.get('password'))
#            if user:
#                _login(request, user)
#                next = request.REQUEST.get('next', '/questions/')
#                return HttpResponseRedirect(next)
#            else:
#                return HttpResponseRedirect(reverse('login'))
#    else:
#        form = LoginForm()
#    rc = RequestContext(request, {'form':form})
#    return render_to_response('login.html', rc)

#def logout(request):
#    _logout(request)
#    return HttpResponseRedirect(reverse('login'))

            