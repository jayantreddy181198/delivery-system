# Generated by Django 5.0.7 on 2024-08-13 04:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('delivered', 'Delivered')], default='pending', max_length=10)),
                ('email', models.EmailField(max_length=255, validators=[django.core.validators.RegexValidator(message='Invalid e-mail.', regex='^([\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4})?$')])),
            ],
        ),
    ]
