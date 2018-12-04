from django.db import models
from django.core.files import File
from urllib import request
import os

from users.models import DeliverUser

# Create your models here.

class Product(models.Model):
    TYPES = {
        ('Verdura', 'VERDURA'),
        ('Fruta', 'FRUTA'),
        ('Electronico', 'ELECTRONICO'),
        ('Bebida', 'BEBIDA'),
    }

    name = models.CharField(max_length=30)
    product_type = models.CharField(max_length=20, choices=TYPES)
    brand = models.CharField(max_length=20)


class Batch(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class Post(models.Model):
    user = models.ForeignKey(DeliverUser, related_name="my_posts", on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    description = models.CharField(max_length=144, blank=True, null=True)
    image_file = models.ImageField(upload_to='images', null=True)
    image_url = models.URLField(null=True)

    def save(self, *args, **kwargs):
        self.get_remote_image()
        super().save(*args, **kwargs)

    def get_remote_image(self):
        if (self.image_url and not self.image_file):
            try:
                result = request.urlretrieve(self.image_url)
                self.image_file.save(
                    os.path.basename(self.image_url),
                    File(open(result[0])))
                self.save()
                
            except Exception as e:
                print(e)
        

class Comment(models.Model):
    user = models.ForeignKey(DeliverUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=128, blank=False, null=False)
