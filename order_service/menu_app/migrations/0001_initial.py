# Generated by Django 5.0.7 on 2024-08-13 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('available', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('Cocktails', 'Cocktails'), ('Beer', 'Beer'), ('Wine', 'Wine'), ('Spirits', 'Spirits'), ('Mocktails', 'Non-Alcoholic Beverages')], max_length=100)),
                ('alcohol_content', models.CharField(choices=[('Strong', 'Strong'), ('Medium', 'Medium'), ('None', 'None')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('available', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('Appetizers', 'Appetizers'), ('Entrees', 'Entrees/Main Courses'), ('Sides', 'Sides/Side Dishes'), ('Desserts', 'Desserts'), ('Beverages', 'Beverages')], max_length=100)),
            ],
        ),
    ]
