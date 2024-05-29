from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name','last_name']
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name','description']
class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['medicine','batch_no', 'expiry_date', 'quantity']
