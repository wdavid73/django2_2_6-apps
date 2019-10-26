from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
    	return reverse("users:user_update" , kwargs={"id" : self.id})


class Cotizacion(models.Model):
    value_cloth         = models.DecimalField(max_digits = 9 ,decimal_places = 2,null = False , default = 0.00)
    value_work          = models.DecimalField(max_digits = 9 ,decimal_places = 2,null = False , default = 0.00)
    value_threads       = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = False , default = 0.00)
    value_buttons       = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = False , default = 0.00)
    value_necks         = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = True , default = 0.00)
    value_embroidery    = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = True , default = 0.00)
    value_prints        = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = True , default = 0.00)
    fashion             = models.CharField(max_length = 50 , null = False)
    # subtotal            = models.DecimalField(max_digits = 10 ,decimal_places = 2,null = False)
    # total               = models.DecimalField(max_digits = 10 ,decimal_places = 2,null = False)
    state               = models.SmallIntegerField(default = 1 , null = False)
    ####################
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)

class User_Cotizacion(models.Model):
    cotizacion          = models.ForeignKey("Cotizacion" , on_delete = models.CASCADE)
    user                = models.ForeignKey("User" , on_delete = models.CASCADE)
    total               = models.DecimalField(max_digits = 10 ,decimal_places = 2,null = False)
    state               = models.SmallIntegerField(default = 1 , null = False)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse("cotizacion:coti_update" , kwargs={"id" : self.id})

