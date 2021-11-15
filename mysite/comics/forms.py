from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from .models import Comics, Images


# TODO:Реализовать форму для создания комикса с одновременным добавлением картинок в модель Images

# class AddComicsForm(forms.ModelForm):
#     title = forms.CharField(max_length=150)
#     description = forms.CharField()
#     is_complete = forms.BooleanField()
#     preview_image = forms.ImageField()

class AddComicsForm(forms.ModelForm):
    class Meta:
        model = Comics
        fields = ['title', 'description', 'is_complete', 'preview_image']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'is_complete': forms.CheckboxInput()
        }


class AtLeastOneFormSet(BaseInlineFormSet):
    def clean(self):
        super(AtLeastOneFormSet, self).clean()
        non_empty_forms = 0
        for form in self:
            if form.cleaned_data:
                non_empty_forms += 1
        if non_empty_forms - len(self.deleted_forms) < 1:
            raise ValidationError("Please fill at least one form.")


class RequiredInlineFormSet(BaseInlineFormSet):

    def _construct_form(self, i, **kwargs):
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        if form.i < 1:
            form.empty_permitted = False
        return form
