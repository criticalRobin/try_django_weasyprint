from django.db import models


# Create your models here.
class ChangeForm(models.Model):
    user = models.CharField(max_length=20)
    project = models.CharField(max_length=35)
    change = models.CharField(max_length=20)
    description = models.TextField()
    REQUEST_STATUS = (
        ("Pending", "Pendiente"),
        ("Approved", "Aprovada"),
        ("Rejected", "Rechazada"),
    )
    status = models.CharField(max_length=10, choices=REQUEST_STATUS, default="Pending")
    date = models.DateField(auto_now_add=True)
