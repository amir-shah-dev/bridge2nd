from django import forms

from .models import Post, CVSection


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CVForm(forms.ModelForm):

    class Meta:
        model = CVSection
        fields = ('title', 'text',)