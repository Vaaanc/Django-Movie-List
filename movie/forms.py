from django import forms
from .models import Movie

class MoviePageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MoviePageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input-text'})
        self.fields['body'].widget.attrs.update({'class': 'input-text'})
        self.fields['is_active'].widget.attrs.update({'class': 'input-checkbox'})
        self.fields['picture'].widget.attrs.update({'class': 'input-picture'})

    class Meta:
        model = Movie
        fields = ('title', 'body', 'is_active', 'picture')

class SoftDeleteForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('picture',)
