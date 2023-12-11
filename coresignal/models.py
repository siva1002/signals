from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    contact=models.CharField(max_length=10,null=True,blank=True)

    class Meta:
        db_table='Contacts'