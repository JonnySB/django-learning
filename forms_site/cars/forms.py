from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        
        fields = "__all__" # pass in all model fields as form fields
        
        labels = {
            'first_name':"Your first name:",
            'last_name':"Your last name:",
            'stars':'Rating:',
        }
        
        error_messages = {
            'stars':{
                'min_value':"Error, the minimum rating is 1",
                'max_value':"Error: the maximum rating is 5"
            }
        }
        