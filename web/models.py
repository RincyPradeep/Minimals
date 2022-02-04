from django.db import models
from django.forms import BooleanField


PRICE_PLAN = (
    ("Standard","Standard"),
    ("Standard Plus","Standard Plus"),
    ("Extended","Extended")
)

class Option(models.Model):
    logo = models.FileField(upload_to="logos/")
    logo_small = models.FileField(upload_to='logos/',blank=True,null=True)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Help(models.Model):
    image = models.FileField(upload_to="helps/")
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title

class Price(models.Model):
    label = models.CharField(max_length=128)
    title = models.CharField(max_length=128,choices = PRICE_PLAN)
    one_end_products = models.BooleanField(default = False)
    twelve_months_updates = models.BooleanField(default = False)
    six_months_of_support = models.BooleanField(default = False)
    javascript_version = models.BooleanField(default = False)
    typescript_version = models.BooleanField(default = False)
    design_resources = models.BooleanField(default = False)
    commercial_applications = models.BooleanField(default = False)

    def __str__(self):
        return self.title
