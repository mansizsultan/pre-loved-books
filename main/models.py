import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='')
    price = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    @property
    def is_book_expensive(self):
        return self.price > 50000

