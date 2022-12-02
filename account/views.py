from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from store.models import Product
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_str
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserEditForm
from . import models


@login_required
def add_wishlist(request, id):
    product = get_object_or_404(Product, id = id)
    if product.users_wishlist.filter(id = request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, product.name + " has been removed from your WishList")
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, "Added " + product.name + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist = request.user)
    return render(request, 'account/user/user_wishlist.html', {'wishlist' : products})

        

@login_required
def dashboard(request):
    return render(request, 'account/user/dashboard.html')

@login_required
def edit_account(request):
    if request.method == "POST":
        user_form = UserEditForm(instance = request.user, data = request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance = request.user)
    return render(request, 'account/user/edit_account.html', {'user_form' : user_form})


@login_required
def delete_profile(request):
    user = models.UserBase.objects.get(username=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')


def account_register(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        # tikrinam forma
        if registerForm.is_valid():
            user = registerForm.save(commit = True)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()

            # current_site = get_current_site(request)
            # subject = _('Activate your account')
            # message = render_to_string('account/registration/account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # user.email_user(subject=subject, message=message)
            return redirect('account:dashboard')
            # HttpResponse(_('registered succesfully'))

    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})


# def account_activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = models.UserBase.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, user.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return redirect('account:dashboard')
#     else:
#         return render(request, 'account/registration/activation_invalid.html')


