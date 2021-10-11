from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import AddComicsForm
from .models import Comics


# def comics_view_page(request):
#     return render(request, 'comics/comics_view_page.html'

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



