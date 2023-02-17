from django.db import models

class All_Employee(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact_no = models.IntegerField(unique=True)
    gender = models.CharField(max_length=500)
    deginations = models.CharField(max_length=50)
    # language = models.CharField(max_length=100)
    # email_id = models.CharField(max_length=500)


