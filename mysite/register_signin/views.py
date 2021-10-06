from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserCreationForm


def authentication(request):
    def valid_form(form, redirect_path_name):
        if form.is_valid():
            form.save()
            return redirect(redirect_path_name)

    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            registration_form = UserRegistrationForm(request.POST)
            valid_form(registration_form, 'authenticate')
        elif request.POST.get('submit') == 'registration':
            sign_in_form = UserCreationForm(request.POST)
            valid_form(sign_in_form, 'home')
    else:
        registration_form = UserRegistrationForm()
        sign_in_form = UserCreationForm()

    context = {
        'registration_form': registration_form,
        'sign_in_form': sign_in_form
    }

    return render(request, 'register_signin/register_page.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('authenticate')
