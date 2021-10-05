from django.shortcuts import render


def register(request):
    return render(request, 'register_signin/register_page.html')
