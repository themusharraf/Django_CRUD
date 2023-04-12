from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=222)

    def __str__(self):
        return self.name


class Person(models.Model):
    fullname = models.CharField(max_length=222)
    email = models.EmailField(max_length=222)
    job = models.ForeignKey('apps.Job', on_delete=models.CASCADE)
    address = models.CharField(max_length=222)
    phone = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to='images')

    def __str__(self):
        return self.fullname
