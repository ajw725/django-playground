from django.db import models

# Create your models here.


class Model(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class User(Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)

    def name(self):
        return f'{self.first_name} {self.last_name} ({self.email})'

    def __str__(self):
        return self.name()
