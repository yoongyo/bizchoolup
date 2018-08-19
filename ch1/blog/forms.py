from django import forms
from .models import Post
from froala_editor.widgets import FroalaEditor

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content']
        widgets = {
            'content': FroalaEditor(),
            'category': forms.Select(
                attrs={
                    'style': 'height: 30px; margin-bottom:15px; width:150px;',
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'style': 'height: 30px; margin-bottom:15px; width:300px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            )
        }

