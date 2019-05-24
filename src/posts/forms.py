from django.forms import ModelForm
from django import forms
from .models import(
    Post
)

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields="__all__"
        exclude=['slug','height_field','width_field']

class SearchForm(forms.Form):
    query=forms.CharField(max_length=40)