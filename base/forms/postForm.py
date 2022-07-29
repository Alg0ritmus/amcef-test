from django.forms import ModelForm
from base.models import Post

class updateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']

class createForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

