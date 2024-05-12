from django.db import models
from django.db.models import CharField


# Model for Products


class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    title = models.CharField(max_length=200)
    price = models.FloatField()
    size_s = models.BooleanField(default=False)
    size_m = models.BooleanField(default=False)
    size_l = models.BooleanField(default=False)
    size_xl = models.BooleanField(default=False)
    description = models.TextField()
    image1 = models.ImageField(upload_to='/media')
    image2 = models.ImageField(upload_to='/media')
    image3 = models.ImageField(upload_to='/media')
    on_hand_quantity = models.IntegerField()
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> CharField:
        return self.title
