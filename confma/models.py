from django.db import models
from django.urls import reverse
from django.utils.timezone import datetime

list_size = [
    ( 'XS'  , 'XS' ),
    ( 'S'   , 'S' ),
    ( 'M'   , 'M' ),
    ( 'L'   , 'L' ),
    ( 'XL'  , 'XL' ),
    ( 'XXL' , 'XXL' ),
]

# Create your models here.
class Client(models.Model):
    name        = models.CharField(max_length = 100 , null = False)
    lastname    = models.CharField(max_length = 200 , null = False)
    address     = models.CharField(max_length = 100 , null = True)
    phone       = models.IntegerField(null = True)
    cellphone   = models.BigIntegerField(null = False)
    #############
    state       = models.SmallIntegerField(default = 1 , null = False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
    	return reverse("users:users_home" , kwargs={"id" : self.id})

    def __str__(self):
        return (self.name + " "+ self.lastname)

class Cloth(models.Model):
    name        = models.CharField(max_length = 100 , null = False)
    color       = models.CharField(max_length = 100 , null = False)
    size        = models.CharField(max_length = 10 ,null = False ,blank = False , choices = list_size , default = 1 )
    #####################
    state       = models.SmallIntegerField(default = 1 , null = False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return (self.name +" "+ ", Talla : " +  self.size +", Color : "+  self.color )



class Cotizacion(models.Model):
    value_cloth         = models.DecimalField(max_digits = 9 ,decimal_places = 2,null = False , default = 0.00)
    value_work          = models.DecimalField(max_digits = 9 ,decimal_places = 2,null = False , default = 0.00)
    value_threads       = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = False , default = 0.00)
    value_buttons       = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = False , default = 0.00)
    value_necks         = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = True , default = 0.00)
    value_embroidery    = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = True , default = 0.00)
    value_prints        = models.DecimalField(max_digits = 8 ,decimal_places = 2,null = True , default = 0.00)
    fashion             = models.CharField(max_length = 50 , null = False)
    cloth               = models.ForeignKey(Cloth , on_delete=models.CASCADE , default  = 1)
    client                = models.ManyToManyField(Client , through="Cotizacion_Client")
    #####################
    state               = models.SmallIntegerField(default = 1 , null = False)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    
    def get_absolute_url(self):
        return reverse("cotizacion:coti_home" , kwargs={"id" : self.id})

    def __str__(self):
        return self.cloth

class Cotizacion_Client(models.Model):
    cotizacion = models.ForeignKey(Cotizacion , on_delete=models.CASCADE)
    client = models.ForeignKey(Client , on_delete=models.CASCADE)
    total = models.BigIntegerField()
    #####################
    state = models.SmallIntegerField(default = 1 , null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


class Alquiler(models.Model):
    date_now    = models.DateField(auto_now_add=True)#[YYYY-MM-DD]
    date_return = models.DateField()#[YYYY-MM-DD]
    price       = models.DecimalField(max_digits = 10 ,decimal_places = 2,null = False , default = 5000.00)
    cloth       = models.ForeignKey(Cloth , on_delete=models.CASCADE)
    client        = models.ForeignKey(Client , on_delete=models.CASCADE)
    #####################
    state = models.SmallIntegerField(default = 1 , null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
