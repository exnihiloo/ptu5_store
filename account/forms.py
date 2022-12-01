from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)
from . import models
from django import forms
from django.utils.translation import gettext_lazy as _


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label=_('Account email (can not be changed)'), max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'})
    )

    username = forms.CharField(
        label=_('Username'), min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'})
    )

    first_name = forms.CharField(
        label=_('First name'), min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'})
    )

    class Meta:
        model = models.UserBase
        fields = ('email', 'username', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True


class RegistrationForm(forms.ModelForm):

        username = forms.CharField(
            label = _("Enter username"),
            min_length = 4,
            max_length = 50,
            help_text = _("Required")
        )

        email = forms.EmailField(
            max_length=100, 
            help_text=_("Required"), 
            error_messages={'required': _('Sorry, you will need an email')}
        )
        
        password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
        password2 = forms.CharField(label=_('Repeat password'), widget=forms.PasswordInput)


        class Meta:
            model = models.UserBase
            fields = ('username', 'email')

        def clean_user_name(self):
            username = self.cleaned_data['user_name'].lower()
            r = models.UserBase.objects.filter(user_name = username)
            if r.count():
                raise forms.ValidationError(_("Username already exists"))
            return username

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError(_('Passwords do not match.'))
            return cd['password2']

        def clean_email(self):
            email = self.cleaned_data['email']
            if models.UserBase.objects.filter(email = email).exists():
                raise forms.ValidationError(_('Please use another Email, that is already taken'))
            return email

        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'Username'})
            self.fields['email'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
            self.fields['password'].widget.attrs.update(
                {'class': 'form-control mb-3', 'placeholder': 'Password'})
            self.fields['password2'].widget.attrs.update(
                {'class': 'form-control', 'placeholder': 'Repeat Password'})


