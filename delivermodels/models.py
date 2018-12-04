from django.db import models

# Create your models here.

class Product(models.model):
    name = models.CharField(max_length=30)

    TYPES = {
        ('Verdura', 'VERDURA'),
        ('Fruta', 'FRUTA'),
        ('Electronico', 'ELECTRONICO'),
        ('Bebida', 'BEBIDA'),
    }

    product_type = models.CharField(max_length=20, choices=TYPES)

    brand = models.CharField(max_length=20)

# Lote
class Batch(models.model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=0)