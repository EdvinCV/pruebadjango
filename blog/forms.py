from django import forms

from .models import Post

class FormPub(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
