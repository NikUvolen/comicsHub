from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import AddComicsForm
from .models import Comics


# def comics_view_page(request):
#     return render(request, 'comics/comics_view_page.html'

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение айпи пользователя
    return ip


class HomeViewComics(ListView):
    model = Comics
    template_name = 'comics/comics_view_page.html'
    context_object_name = 'comics'

    def get_queryset(self):
        return Comics.objects.filter(is_complete=True)


class ViewComicsDetail(DetailView):
    model = Comics
    template_name = 'comics/comics_detail_view_page.html'
    pk_url_kwarg = 'comics_id'
    context_object_name = 'comics'


# Todo: https://ru.stackoverflow.com/questions/1233137/django-Как-реализовать-счетчик-просмотров-БЕЗ-НАКРУТКИ


# TODO: Переписать add_comics
def add_comics(request):
    if request.method == 'POST':
        comics_form = AddComicsForm(request.POST, request.FILES)

        if comics_form.is_valid():
            comics_form.save()
            return redirect('home')
    else:
        comics_form = AddComicsForm()

    context = {
        'comics_form': comics_form,
    }
    return render(request, 'comics/add_comics.html', context=context)


