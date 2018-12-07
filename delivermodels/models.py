from django.db import models
from users.models import DeliverUser


# Create your models here.


class Post(models.Model):
    TYPES = {
        ('Verduras', 'VERDURAS'),
        ('Frutas', 'FRUTAS'),
        ('Electrodomesticos', 'ELECTRODOMESTICOS'),
        ('Bebidas', 'BEBIDAS'),
        ('Electronica', 'ELECTRONICA'),
        ('Ropa', 'ROPA'),
        ('Accesorios', 'ACCESORIOS'),
        ('Inmuebles', 'INMUEBLES'),
        ('Juguetes', 'JUGUETES'),
    }

    product_name = models.CharField(max_length=30)
    user = models.ForeignKey(DeliverUser, related_name="my_posts", on_delete=models.CASCADE)
    description = models.CharField(max_length=144, blank=True, null=True)
    product_description = models.CharField(max_length=144, blank=True, null=True)
    image_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=50, blank=True)
    product_type = models.CharField(max_length=20, choices=TYPES, blank=True)
    brand = models.CharField(max_length=20, blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    stock = models.PositiveIntegerField(default=0, blank=True)


class Question(models.Model):
    user = models.ForeignKey(DeliverUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=128, blank=False, null=False)


class Answer(models.Model):
    user = models.ForeignKey(DeliverUser, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
