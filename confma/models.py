from django.db import models

# Create your models here.
class User(models.Model):
    name        = models.CharField(),
    lastname    = models.CharField(),
    address     = models.CharField(),
    phone       = models.IntegerField(),
    cellphone   = models.IntegerField(),
    state       = models.BinaryField(),
    ##########################################3
    created_at  = models.DateTimeField(auto_now_add=True),
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'confma_users'