from django.db import models

class Product(models.Model):
    mood = models.CharField(max_length=100) # nama produk disini
    price = models.DecimalField(max_digits=10, decimal_places=2)  # harga produk
    description = models.TextField()  # deskripsi produk

    def __str__(self):
        return self.name