from django.db import models

# Create your models here.
class User(models.Model):
    name        = models.CharField(max_length = 100 , null = False)
    lastname    = models.CharField(max_length = 200 , null = False)
    address     = models.CharField(max_length = 100 , null = True)
    phone       = models.IntegerField(null = True)
    cellphone   = models.BigIntegerField(null = False)
    state       = models.SmallIntegerField(default = 1 , null = False)
    ##########################################
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now = True)