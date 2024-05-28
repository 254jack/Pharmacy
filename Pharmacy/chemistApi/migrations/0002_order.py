# Generated by Django 5.0.6 on 2024-05-28 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemistApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('medicine', models.ManyToManyField(to='chemistApi.medicine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemistApi.user')),
            ],
        ),
    ]