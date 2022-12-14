from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **kwargs):

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned to is_staff = True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be assigned to is_superuser = True.'))

        return self.create_user(email, username, password, **kwargs)

    def create_user(self, email, username, password, **kwargs):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **kwargs)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=150, unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    about = models.TextField(_('about'), max_length=500, blank=True)
    country = models.CharField(_("country"), max_length=200)
    phone_number = models.CharField(_('phone number'), max_length=15, blank=True)
    postcode = models.CharField(_('post code'), max_length=12, blank=True)
    address_line_1 = models.CharField(_('adress 1'), max_length=150, blank=True)
    address_line_2 = models.CharField(_('adress 2'), max_length=150, blank=True)
    town_city = models.CharField(_('city'), max_length=150, blank=True)
    is_active = models.BooleanField(_('is active'), default=False)
    is_staff = models.BooleanField(_('is staff'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.username
