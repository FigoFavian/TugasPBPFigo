from django.db import models

class Product(models.Model):
    mood = models.CharField(max_length=100) # nama produk disini
    price = models.IntegerField()  # harga produk
    description = models.TextField()  # deskripsi produk
