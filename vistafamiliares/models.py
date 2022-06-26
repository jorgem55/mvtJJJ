from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
class familia(models.Model):
    nombre=models.CharField()
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField(null=True)