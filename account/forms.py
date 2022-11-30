from . import models
from django import forms
from django.utils.translation import gettext_lazy as _


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