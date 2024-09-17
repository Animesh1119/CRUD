from django.db import models

# Create your models here.
class mydb(models.Model):
    prodid = models.AutoField
    prodname = models.CharField(max_length=50)
    prodphone = models.IntegerField()

    # def __str__(self):
    #     print(self.prodname)