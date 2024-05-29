from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView,ListView,UpdateView,DeleteView
from django.views.generic import CreateView
from .forms import Medicine, MedicineForm,UserCreationForm,UserRegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout as auth_logout
from django.utils.decorators import method_decorator
from django.contrib import messages


@login_required
def index(request):
    medicines = Medicine.objects.all()
    return render(request, 'index.html', {'medicines': medicines})

@method_decorator(login_required, name='dispatch')
class MedicineListView(ListView):
    model = Medicine
    template_name = 'medicine_list.html'
    context_object_name = 'medicines'
@method_decorator(login_required, name='dispatch')
class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine_form.html'
    success_url = reverse_lazy('medicine_list')

@method_decorator(login_required, name='dispatch')
class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'medicine_confirm_delete.html'
    success_url = reverse_lazy('medicine_list')
@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine_name = form.cleaned_data['name']
            if Medicine.objects.filter(name=medicine_name).exists():
                messages.error(request, f'Medicine with the name "{medicine_name}" already exists.')
            else:
                form.save()
                messages.success(request, 'Medicine added successfully.')
                return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'login.html'


def logout(request):
    if request.method in ['POST', 'GET']:
        auth_logout(request)
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

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
