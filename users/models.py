from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class DeliverUser(AbstractUser):

    USER_TYPE_CHOICES = (
        (1, 'Mayorista'),
        (2, 'Minorista'),
        (3, 'Empleado'),
        (4, 'Admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=4)


class Mayorista(models.Model):

    TAX_CONDITION_CHOICES = (
        (1, 'Responsable inscripto'),
        (2, 'Responsable no inscripto'),
        (3, 'Monotribustista'),
    )

    def validate_CUIT(CUIT):
        CUIT = str(CUIT)
        CUIT = CUIT.replace("-", "")
        CUIT = CUIT.replace(" ", "")
        CUIT = CUIT.replace(">.", "")

        if (len(CUIT) != 11):
            return False

        if (not CUIT.isdigit()):
            return False

        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        aux = 0

        for i in range(0, 10):
            aux += int(CUIT[i]) * base[i]

        aux = 11 - (aux % 11)

        if (aux == 11):
            aux = 0

        if (int(CUIT[10]) == aux):
            return True
        else:
            return False

    user = models.OneToOneField(
        DeliverUser, on_delete=models.CASCADE, primary_key=True, related_name="DeliverUser")
    CUIT = models.CharField(max_length=11,
                            null=False, validators=[validate_CUIT], blank=False)
    registered_name = models.CharField(max_length=25, null=False, blank=True)
    CBU = models.CharField(max_length=22, null=True, blank=True)
    tax_condition = models.IntegerField(choices=TAX_CONDITION_CHOICES, blank=True)



class Minorista(models.Model):
    user = models.OneToOneField(
        DeliverUser, on_delete=models.CASCADE, primary_key=True)
    Tipo_Comercio = models.CharFiel(max_length=50, null=False, blank=True)
    CUIT = models.IntegerField(null=True, blank=True)
    registered_name = models.CharField(max_length=25, null=False, blank=True)


class Empleado(models.Model):
    user = models.OneToOneField(
        DeliverUser, on_delete=models.CASCADE, primary_key=True)
    Sueldo = models.IntegerField(max_length=5, blank=True)
    Nombre = models.CharField(max_length=50, blank=True)
    Apellido = models.CharField(max_length=50, blank=True)
    Numero_de_legajo = models.ManyToManyField(Minorista, Mayorista, blank=False)
    Telefono = models.CharField(max_length=10, blank=True)
