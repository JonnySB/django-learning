from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name',max_length=100)
#     last_name = forms.CharField(label='Last Name',max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here',
#                              widget=forms.Textarea(attrs={
#                                                     'class':'my_form',
#                                                     'row':'18',
#                                                     'cols':'80',    
#                                                 }))


