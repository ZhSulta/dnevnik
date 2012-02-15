from accounts.forms import EmailLoginForm, EmailRegistrationForm

def login_form(request):
    login_form = EmailLoginForm()
    return {'login_form' : login_form}

def register_form(request):
    register_form = EmailRegistrationForm()
    return {'register_form' : register_form}
