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
    image_url = models.URLField(null=True)
    title = models.CharField(max_length=50, blank=False)
    product_type = models.CharField(max_length=20, choices=TYPES)
    brand = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)


class Question(models.Model):
    user = models.ForeignKey(DeliverUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=128, blank=False, null=False)


class Answer(models.Model):
    user = models.ForeignKey(DeliverUser, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

