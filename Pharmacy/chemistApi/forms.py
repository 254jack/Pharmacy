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
        fields = ['name','supplier','description']
class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['medicine','supplier','batch_no', 'expiry_date', 'quantity']



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['order_date']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone_number']
