from django.db import models

class UrlForm(models.Model):
    name = models.CharField(max_length=130)
    url = models.URLField()
    PhoneNum= models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Search(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

