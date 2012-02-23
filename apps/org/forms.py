from django import forms
from django.contrib.auth.models import User
from apps.models.models import School, City, Temporary


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'minlength':'6'}))

class School_reg_form(forms.ModelForm):
    class Meta:
        model = School
        #exclude = ['org']  

class City_add_form(forms.ModelForm):
    class Meta:
        model = City        
    
class TemporaryForm(forms.ModelForm):
    number = forms.IntegerField(max_value = 100, min_value = 1)        
    class Meta:
        model = Temporary
        exclude = ('username','pwd','role')

class RegisterForm(forms.Form):
    
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'minlength':'6'}))
    cpassword = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'minlength':'6'}))
    #file=forms.FileField()
    
    def clean(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        
        if password != cpassword:
            raise forms.ValidationError('Password mismatch!')
        return self.cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        q = User.objects.filter(username=username)
        
        if q.count():
            raise forms.ValidationError('Username already exists!')
        return username
    
class EditingForm(forms.ModelForm):
#    username = forms.CharField(max_length=20)
#    first_name = forms.CharField(max_length=20)
#    email = forms.EmailField()
    class Meta:
        model = User
        exclude = ('username','password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions')

