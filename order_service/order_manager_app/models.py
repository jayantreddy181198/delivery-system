from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class OrderItems(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('delivered', 'Delivered'),
    ]
    items = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    email = models.EmailField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^([\w\.\-]+@([\w\-]+\.)+[\w\-]{2,4})?$',
                message='Invalid e-mail.'
            )
        ],
        blank=False
    )

    def __str__(self):
        return f"Order #{self.pk} - {self.status}"