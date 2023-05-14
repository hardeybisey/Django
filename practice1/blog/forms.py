from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError('hoo hoo')
        return title
