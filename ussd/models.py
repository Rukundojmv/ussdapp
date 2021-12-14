from django.db import models
from datetime import date, datetime
# Create your models here.
class Idafarmuser(models.Model):
    
    sessiondId = models.CharField(max_length=255, null=True)
    serviceCode = models.CharField(max_length=255, null=True)
    phoneNumber = models.CharField(max_length=255)
    level  = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sizeOfland = models.CharField(max_length=255)
    names = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.phoneNumber


class Iteganyagihe(models.Model):
    sessionId = models.CharField(max_length=255, null=True)
    phonNumber = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.phonNumber







class chiaCustomer(models.Model):
    
    phoneNumber = models.CharField(max_length=255)
    fullName = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    purchasedTime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.fullName