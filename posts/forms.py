from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'photo'
        ]
        labels = {
            'title': "제목",
            'content': "내용",
            'photo' : "사진"
        }
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        labels = {
            'content': "내용",
        }
        