from django.contrib import admin

from .models import User, Medicine, Supplier, Prescription, Sale

admin.site.register(User)
admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Prescription)
admin.site.register(Sale)
