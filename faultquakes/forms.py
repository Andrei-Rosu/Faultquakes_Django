from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post


# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea


# If you don't like <iframe>, then use inplace widget
# Or if you're using django-crispy-forms, please use this.
class PostForm(forms.Form):
    content = forms.CharField(widget=SummernoteInplaceWidget())


class FormFromPostModel(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)
        widgets = {
            'content': SummernoteInplaceWidget(),
        }

