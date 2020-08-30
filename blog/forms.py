from django import forms

from .models import Post, CVSection

EMPTY_TITLE_ERROR = "You can't leave the title field empty"
EMPTY_TEXT_ERROR = "You can't leave the text field empty"


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        error_messages = {
            'title': {'required': EMPTY_TITLE_ERROR},
            'text': {'required': EMPTY_TEXT_ERROR}
        }


class CVForm(forms.ModelForm):

    class Meta:
        model = CVSection
        fields = ('title', 'text',)

        error_messages = {
            'title': {'required': EMPTY_TITLE_ERROR},
            'text': {'required': EMPTY_TEXT_ERROR}
        }
