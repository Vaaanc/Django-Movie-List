from django import forms
from .models import Movie


class MoviePageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MoviePageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'input-text',
            'placeholder': 'Enter movie title here'
            })
        self.fields['body'].widget.attrs.update({
            'class': 'input-text',
            'placeholder': 'Enter body text here',
            'rows': '16'
            })
        self.fields['picture'].widget.attrs.update({
        'class': 'input-picture'
        })

    class Meta:
        model = Movie
        fields = ('title', 'body', 'picture')
