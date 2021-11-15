from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from .models import UserProfiles, User


def view_user_profile(request, username):
    user_profile = get_object_or_404(User.objects.select_related('userprofiles'), username=username)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'user_profiles/profile.html', context=context)


def redirect_to_comics(request):
    return redirect('home')
