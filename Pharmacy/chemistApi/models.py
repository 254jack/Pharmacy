from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Changed related_name to be unique
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Changed related_name to be unique
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='e.g supplier@gmail.com')
    phone_number = models.CharField(max_length=20, default='e.g 1234567890')

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    description = models.TextField(default='No description provided')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    prescribed_date = models.DateField(auto_now_add=True)
    dosage = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.medicine.name}"

class EPrescription(models.Model):
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)
    doctor_email = models.EmailField()
    signature = models.CharField(max_length=255)
    issued_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"E-Prescription for {self.prescription.customer_name}"

class Batch(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='batches')
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE)
    batch_no = models.CharField(max_length=100)
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.medicine.name} - {self.supplier.name}"

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.medicine.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sale of {self.medicine.name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    medicine = models.ForeignKey(Medicine, related_name='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.medicine.name} on {self.order_date}"
