from django.contrib.auth.models import User
from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.PositiveIntegerField()
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
