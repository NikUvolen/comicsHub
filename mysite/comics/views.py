from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import AddComicsForm
from .models import Comics, Ip


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

    def get_queryset(self):
        return Comics.objects.filter(is_complete=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        comics = Comics.objects.prefetch_related('views').all()

        paginator = Paginator(comics, 4)
        comics_page_number = self.request.GET.get('page')
        comics_page_obj = paginator.get_page(comics_page_number)

        context['comics_page_obj'] = comics_page_obj
        return context


class ViewComicsDetail(DetailView):
    model = Comics
    template_name = 'comics/comics_detail_view_page.html'
    slug_url_kwarg = 'comics_slug'
    context_object_name = 'comics'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        comics = Comics.objects.prefetch_related('images_set').get(pk=kwargs['object'].pk)
        ip = get_client_ip(self.request)

        if Ip.objects.filter(ip=ip).exists():
            comics.views.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            comics.views.add(Ip.objects.get(ip=ip))

        context['comics'] = comics
        return context


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


