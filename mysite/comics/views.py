from django.shortcuts import render


def comics_view_page(request):
    return render(request, 'comics/comics_view_page.html')
