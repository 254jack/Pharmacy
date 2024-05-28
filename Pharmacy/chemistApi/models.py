from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='Chemist_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(Permission,
                                              related_name='chemist_user_set',
                                              blank=True,
                                              help_text='Specific permissions for this user.',
                                              verbose_name='user permissions',
                                              )


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=100)
    expiry_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact = models.TextField()

    def __str__(self):
        return self.name


class Prescription(models.Model):
    customer_name = models.CharField(max_length=100)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    prescribed_date = models.DateField(auto_now_add=True)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_name} - {self.medicine.name}"


class Sale(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Sale of {self.medicine.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')