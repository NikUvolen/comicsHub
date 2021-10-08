from django import forms
from django.conf import settings

from .models import Comics, Images


# TODO:Реализовать форму для создания комикса с одновременным добавлением картинок в модель Images

class AddComicsForm(forms.Form):
    title = forms.CharField(max_length=150)
    description = forms.CharField()
    is_complete = forms.BooleanField()
    preview_image = forms.ImageField()

# class AddComicsForm(forms.ModelForm):
#     class Meta:
#         model = Comics
#         fields = ['title', 'description', 'is_complete']
#         widgets = {
#             'title': forms.TextInput(),
#             'description': forms.Textarea(),
#             'is_complete': forms.CheckboxInput()
#         }
#
# class AddImageForm(forms.ModelForm):

