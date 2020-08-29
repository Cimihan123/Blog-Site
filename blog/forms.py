from .models import Contact, Comment, Post
from django.forms import ModelForm
from django import forms


class contactForm(forms.ModelForm):
  
    class Meta:

        model = Contact

        fields = '__all__'
     

class commentForm(forms.ModelForm):
  
    class Meta:

        model = Comment

        fields = '__all__'
        exclude = ['post']
     

     
class postForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title'}))
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'placeholder': 'name'})
    )
    class Meta:
        model = Post 
        fields = '__all__'