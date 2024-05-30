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

    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', views.CustomerCreateView.as_view(),
         name='create_customer'),
    path('customers/update/<int:pk>/',
         views.CustomerUpdateView.as_view(), name='update_customer'),
    path('customers/delete/<int:pk>/',
         views.CustomerDeleteView.as_view(), name='delete_customer'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/create/', views.OrderCreateView.as_view(), name='create_order'),
    path('orders/update/<int:pk>/',
         views.OrderUpdateView.as_view(), name='update_order'),
    path('orders/delete/<int:pk>/',
         views.OrderDeleteView.as_view(), name='delete_order'),

    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/add/', views.add_supplier, name='add_supplier'),
    path('suppliers/edit/<int:pk>/', views.edit_supplier, name='update_supplier'),
    path('suppliers/delete/<int:pk>/',
         views.delete_supplier, name='delete_supplier'),


    path('prescriptions/', views.list_prescriptions, name='list_prescriptions'),
    path('prescriptions/create/', views.create_prescription, name='create_prescription'),
    path('prescriptions/verify/<int:pk>/',
         views.verify_prescription, name='verify_prescription'),
    path('prescriptions/delete/<int:pk>/', views.delete_prescription, name='delete_prescription'),

    path('e-prescriptions/', views.list_e_prescriptions, name='list_e_prescriptions'),
    path('e-prescriptions/create/', views.create_e_prescription,
         name='create_e_prescription'),
     path('e-prescriptions/delete/<int:pk>/', views.delete_e_prescription, name='delete_e_prescription'),
     
     path('sales/', views.sale_list, name='sale_list'),
     path('sales/new/', views.sale_create, name='sale_create'),
    
]
