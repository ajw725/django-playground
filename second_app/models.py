from django.db import models

# Create your models here.


class Model(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Topic(Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Webpage(Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
