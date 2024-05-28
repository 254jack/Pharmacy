# chemistApi/urls.py
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('add_medicine/', TemplateView.as_view(template_name='add_medicine.html'), name='add_medicine'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('logged_out/', TemplateView.as_view(template_name='logged_out.html'), name='logged_out'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
]