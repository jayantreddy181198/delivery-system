from django.db import models

# Model for food items on the menu
class FoodItem(models.Model):

    CATEGORY_CHOICES = [
        ('Appetizers', 'Appetizers'),
        ('Entrees', 'Entrees/Main Courses'),
        ('Sides', 'Sides/Side Dishes'),
        ('Desserts', 'Desserts'),
        ('Beverages', 'Beverages'),
    ]


    name = models.CharField(max_length=100)  # Name of the food item
    description = models.TextField(blank=True)  # Optional description
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the food item
    available = models.BooleanField(default=True)  # Whether the food item is available
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


# Model for bar (drink) items on the menu
class BarItem(models.Model):

    CATEGORY_CHOICES = [
        ('Cocktails', 'Cocktails'),
        ('Beer', 'Beer'),
        ('Wine', 'Wine'),
        ('Spirits', 'Spirits'),
        ('Mocktails', 'Non-Alcoholic Beverages'),
    ]

    ALCOHOL_CONTENT = [
        ('Strong', 'Strong'),
        ('Medium', 'Medium'),
        ('None', 'None'),
    ]

    name = models.CharField(max_length=100)  # Name of the bar item (drink)
    description = models.TextField(blank=True)  # Optional description
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the drink
    available = models.BooleanField(default=True)  # Whether the drink is available
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES) # Category of alcohol
    alcohol_content = models.CharField(max_length=100, choices=ALCOHOL_CONTENT)  # Alcohol content percentage

    def __str__(self):
        return self.name