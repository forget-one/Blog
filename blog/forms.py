from django import forms
from .models import *
from django.core.exceptions import ValidationError
# Create your models here.






class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput()
            }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError("Slug can't be 'create'")
        if Tag.objects.filter(slug=new_slug).count():
            raise ValidationError('slug must be unique. "{}" slug already exists'. format(new_slug))
        return new_slug

    


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'body': forms.Textarea(attrs={'id': 'textarea1', 'class': 'materialize-textarea'}),
            'tags': forms.SelectMultiple(),
            }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()
            if new_slug == 'create':
                raise ValidationError("Slug can't be 'create'")
            return new_slug
