from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import User

# Model for Products


class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    mrp_price = models.FloatField(null=True, default=0.0)
    size_s = models.BooleanField(default=False)
    size_m = models.BooleanField(default=False)
    size_l = models.BooleanField(default=False)
    size_xl = models.BooleanField(default=False)
    description = models.TextField()
    image1 = models.ImageField(upload_to='media/')
    image2 = models.ImageField(upload_to='media/')
    image3 = models.ImageField(upload_to='media/')
    on_hand_quantity = models.IntegerField()
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


# dynamic content in hero section
class BannerContent(models.Model):
    banner_image1 = models.ImageField(upload_to='media/')
    banner_image2 = models.ImageField(upload_to='media/')
    banner_title1 = models.CharField(max_length=100)
    banner_title2 = models.CharField(max_length=100)
    banner_subtitle1 = models.CharField(max_length=100)
    banner_subtitle2 = models.CharField(max_length=100)
    banner_desc1 = models.CharField(max_length=100)
    banner_desc2 = models.CharField(max_length=100)


class ReadBlogs(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_image = models.ImageField(upload_to='media/')
    blog_content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title


class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject
    