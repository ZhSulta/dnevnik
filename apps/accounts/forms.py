# encoding: utf-8
from django.template import Context, Template
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from dnevniktools.dbutils import get_nextautoincrement
from django.contrib.auth.models import User
from models.models import StudentProfile


from uni_form import helpers
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.utils.http import int_to_base36
from django.template import loader

attrs_dict = { 'class': 'required' }

try:
    # If you have django-registration installed, this is a form you can
    # use for users that signup.
    from registration.forms import RegistrationFormUniqueEmail
    class EmailRegistrationForm(RegistrationFormUniqueEmail):

        @property
        def helper(self):
            """ We call this as a method/property so we don't make the form helper a singleton. """

            # instantiate the form helper object
            helper = helpers.FormHelper()

            # add in some input controls (a.k.a. buttons)
            submit = helpers.Submit('submit',_('Registration'))
            helper.add_input(submit)
            helper.form_action = reverse('email-register')

            helper.form_method = 'POST'

            return helper


        def __init__(self, *args, **kwargs):
            super(EmailRegistrationForm, self).__init__(*args, **kwargs)
            del self.fields['username']

        def save(self, *args, **kwargs):
            # Note: if the username column has not been altered to allow 75 chars, this will not
            #       work for some long email addresses.
            next_id = get_nextautoincrement(User)
            self.cleaned_data['username'] = "user%05d" % next_id
            return super(EmailRegistrationForm, self).save(*args, **kwargs)
except ImportError:
    pass

class EmailLoginForm(forms.Form):
    email = forms.CharField(label = _("Email"), max_length = 75, widget = forms.TextInput(attrs = dict(maxlength = 75)))
    password = forms.CharField(label = _(u"Password"), widget = forms.PasswordInput)
    next = forms.CharField(widget = forms.HiddenInput, required = False, max_length = 255)

    @property
    def helper(self):
        """ We call this as a method/property so we don't make the form helper a singleton. """

        # instantiate the form helper object
        helper = helpers.FormHelper()

        # add in some input controls (a.k.a. buttons)
        submit = helpers.Submit('submit',_('Enter'))
        helper.add_input(submit)
        helper.form_class = 'small-login'

        return helper

    def clean(self):
        # Try to authenticate the user
        if self.cleaned_data.get('email') and self.cleaned_data.get('password'):
            user = authenticate(username = self.cleaned_data['email'], password = self.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    self.user = user # So the login view can access it
                else:
                    t = Template('<a href="javascript:error_toggle();"><font class="errortext" style="top: 0px;">Этот логин не активный.<br></font></a>')
                    c = Context()
                    raise forms.ValidationError(t.render(c))
            else:
                raise forms.ValidationError(_('Invalid email or password.'))
        return self.cleaned_data

class ClientProfileForm(forms.ModelForm):
        
    first_name = forms.CharField(label = _('Name:'), max_length = 30, required = False)
    last_name = forms.CharField(label = _('Last name:'), max_length = 30, required = False)
    password1 = forms.CharField(label = _('New password'), widget = forms.PasswordInput, required = False)
    password2 = forms.CharField(label = _("Confirm new password:"), widget = forms.PasswordInput, required = False)

    class Meta:
        model = StudentProfile
        fields = ('first_name', 'last_name', 'address', 'mobile', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:            
            raise forms.ValidationError(_('Incorrect confirmation password.'))                
        return password2

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """        
        if User.objects.filter(email__iexact=self.cleaned_data['email']).exclude(User.objects.get(pk=self.pk)):
            raise forms.ValidationError(_('This e-mail is already used.'))               
        return self.cleaned_data['email']

    @property
    def helper(self):
        """ We call this as a method/property so we don't make the form helper a singleton. """

        # instantiate the form helper object
        helper = helpers.FormHelper()

        # add in some input controls (a.k.a. buttons)
        submit = helpers.Submit('submit', _('Save'))
        helper.add_input(submit)

        helper.form_method = 'POST'
        helper.form_class = 'uniform'
        helper.form_id = 'adduser-form-id'
        return helper

class EditingForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ('username', 'password', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions')

    @property
    def helper(self):
        """ We call this as a method/property so we don't make the form helper a singleton. """

        # instantiate the form helper object
        helper = helpers.FormHelper()

        # add in some input controls (a.k.a. buttons)
        submit = helpers.Submit('submit',_('Save'))
        helper.add_input(submit)

        return helper

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        
        if User.objects.filter(email__iexact=self.cleaned_data['email']).exclude(User.objects.get(user = self)):            
            raise forms.ValidationError(_('This e-mail is already used.'))               
        return self.cleaned_data['email']
    

class ChangeGiftForm(forms.Form):
    email = forms.EmailField(max_length=75)
    
    def __init__(self, *args, **kw):
        self.instance = kw.get('instance', None)
        if self.instance:
            del kw['instance']
            kw['initial'] = {'email': self.instance.giftant_email}
        super(ChangeGiftForm, self).__init__(*args, **kw)

    def save(self, *a, **kw):
        self.instance.giftant_email = self.cleaned_data.get('email')
        self.instance.save()
        
class PasswordResetForm(forms.Form):
    email = forms.EmailField(label=_("E-mail"), max_length=75)

    def clean_email(self):
        """
        Validates that an active user exists with the given e-mail address.
        """
        email = self.cleaned_data["email"]
        self.users_cache = User.objects.filter(
                                email__iexact=email,
                            )
        if len(self.users_cache) == 0:
            raise forms.ValidationError(_("That e-mail address doesn't have an associated user account. Are you sure you've registered?"))
        return email

    def save(self, domain_override=None, email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator, from_email=None, request=None):
        """
        Generates a one-use only link for resetting password and sends to the user
        """
        from django.core.mail import send_mail
        for user in self.users_cache:
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            t = loader.get_template(email_template_name)
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': int_to_base36(user.id),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': use_https and 'https' or 'http',
            }
            send_mail(_("Password reset on %s") % site_name,
                t.render(Context(c)), from_email, [user.email])

class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set his/her password without
    entering the old password
    """
    new_password1 = forms.CharField(label=_("New password"), widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_("New password confirmation"), widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])        
        if commit:
            self.user.save()
        return self.user
