from django import forms

from pagedown.widgets import PagedownWidget
from django.utils import timezone
from .models import Post




class PostForm1(forms.ModelForm):
    experience_required = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    
    class Meta:
        model = Post
        fields = [
            "title",
            "salary",
        ]

class PostForm2(forms.ModelForm):
    experience_required = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    
    class Meta:
        model = Post
        fields = [
            "experience_required",
            "draft",
            "publish",
        ]

class PostForm3(forms.ModelForm):
    experience_required = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    
    class Meta:
        model = Post
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",  
        ]
