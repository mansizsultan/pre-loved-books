import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='')
    price = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.TextField()
    
    @property
    def is_book_expensive(self):
        return self.price > 50000

