from django.db import models

# ------------------- VENDOR MODEL -------------------
class Vendor(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    


# ------------------- CUSTOMER MODEL -------------------
class Customer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    


# ------------------- BIRD PRODUCT MODEL -------------------
class BirdProduct(models.Model):
    BIRD_TYPES = [
        ('rooster', 'Rooster'),
        ('hen', 'Hen'),
        ('chick', 'Chick'),
    ]

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    bird_type = models.CharField(max_length=10, choices=BIRD_TYPES)
    niram = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    age = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to="bird_images/")
    video = models.FileField(upload_to="bird_videos/", null=True, blank=True)
    father_image = models.ImageField(upload_to="bird_images/")
    father_video = models.FileField(upload_to="bird_videos/", null=True, blank=True)

    

class Admin(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user_type = models.CharField(max_length=10)  # 'customer' or 'vendor'
    message = models.TextField()



