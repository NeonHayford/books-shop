from .models import *
from django import forms

# class bookforms(forms.ModelForm):
#     class Meta:
#         models = Book
#         fields = '__all__'

class BookStatusForm(forms.ModelForm):
    class Meta:
        models = BookStatus
        fields = '__all__'

class SubscriptionForm(forms.ModelForm):
    class Meta:
        models = Subscription
        fields = '__all__'