from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout as auth_logout
from django.contrib import messages


@login_required
def index(request):
    medicines = Medicine.objects.all()
    return render(request, 'index.html', {'medicines': medicines})


@login_required
def add_medicine(request):
    if request.method == 'POST':
        name = request.POST['name']
        batch_no = request.POST['batch_no']
        expiry_date = request.POST['expiry_date']
        quantity = request.POST['quantity']
        Medicine.objects.create(
            name=name, batch_no=batch_no, expiry_date=expiry_date, quantity=quantity)
        return redirect('index')
    return render(request, 'add_medicine.html')


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'login.html'


def logout(request):
    if request.method in ['POST', 'GET']:
        auth_logout(request)
        messages.info(request, 'You have successfully logged out.')
        return redirect('logged_out')
    return redirect('index')

@login_required
def dashboard(request):
    num_medicines = Medicine.objects.count()
    num_prescriptions = Prescription.objects.count()
    num_orders = Order.objects.count()
    context = {
        'num_medicines': num_medicines,
        'num_prescriptions': num_prescriptions,
        'num_orders': num_orders,
    }
    return render(request, 'dashboard.html', context)

