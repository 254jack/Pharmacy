# chemistApi/urls.py
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('logged_out/', TemplateView.as_view(template_name='logged_out.html'),
         name='logged_out'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'),
         name='dashboard'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
    path('medicines/', views.MedicineListView.as_view(), name='medicine_list'),
    path('medicines/update/<int:pk>/',
         views.MedicineUpdateView.as_view(), name='medicine_update'),
    path('medicines/delete/<int:pk>/',
         views.MedicineDeleteView.as_view(), name='medicine_delete'),
    path('batches/', views.BatchListView.as_view(), name='batch_list'),
    path('batches/add/', views.add_batch, name='add_batch'),
    path('batches/update/<int:pk>/',
         views.BatchUpdateView.as_view(), name='batch_update'),
    path('batches/delete/<int:pk>/',
         views.BatchDeleteView.as_view(), name='batch_delete'),
]
