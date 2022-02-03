from django.db import models


class Option(models.Model):
    logo = models.FileField(upload_to="logos/")
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
