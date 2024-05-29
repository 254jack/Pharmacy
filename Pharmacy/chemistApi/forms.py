from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Medicine

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'batch_no', 'expiry_date', 'quantity']
