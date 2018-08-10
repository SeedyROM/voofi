from django.forms.models import ModelForm

from .models import Like, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('body',)