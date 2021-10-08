from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import AddComicsForm
from .models import Comics, Images


def comics_view_page(request):
    return render(request, 'comics/comics_view_page.html')


# TODO: Переписать add_comics
def add_comics(request):
    if request.method == 'POST':
        comics_form = AddComicsForm(request.POST, request.FILES)

        if comics_form.is_valid():
            comics = Comics.objects.create(
                title=comics_form['title'],
                description=comics_form['description'],
                is_complete=comics_form['is_complete'],
                author_id=request.user
            )
            Images.objects.create(
                comics_id=comics,
                preview_image=comics['preview_image']
            )
            print(comics)
            return redirect(comics)
    else:
        comics_form = AddComicsForm()

    context = {
        'comics_form': comics_form,
    }
    return render(request, 'comics/add_comics.html', context=context)



