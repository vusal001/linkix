from .models import Link
from django import forms


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ('name', 'link', 'linktype')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {'placeholder': 'link'}


        