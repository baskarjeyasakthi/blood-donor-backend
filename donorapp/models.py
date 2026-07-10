from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    district = models.CharField(max_length=100)
    lastDonated = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name



     