from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserLoginForm
from mysite.decorators import anonymous_required


@anonymous_required(redirect_url='/')
def authentication(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        sign_in_form = UserLoginForm(data=request.POST)
        if request.POST.get('submit') == 'registration':
            if registration_form.is_valid():
                registration_form.save()
                return redirect('authentication')
        elif request.POST.get('submit') == 'sign_in':
            if sign_in_form.is_valid():
                user = sign_in_form.get_user()
                login(request, user)
                return redirect('home')
    else:
        registration_form = UserRegistrationForm()
        sign_in_form = UserLoginForm()

    context = {
        'registration_form': registration_form,
        'sign_in_form': sign_in_form
    }

    return render(request, 'register_signin/register_page.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('authentication')
