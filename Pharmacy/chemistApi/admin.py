from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Prescription)
admin.site.register(EPrescription)
admin.site.register(Sale)
admin.site.register(Customer)
admin.site.register(Order)
