from django.db import models

list_size = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
]


class Client(models.Model):
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    cellphone = models.BigIntegerField(null=False)
    #############
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lookup_field = 'pk'

    def __str__(self):
        return self.name + " " + self.lastname + " - " + str(self.cellphone)

    class Meta:
        db_table = "Client"


class Cloth(models.Model):
    name = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False)
    size = models.CharField(max_length=10, null=False, blank=False, choices=list_size, default=1)
    fashion = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='fashion/%Y/%m/%d/')
    #####################
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lookup_field = 'pk'

    def __str__(self):
        return self.name + " " + ", Talla : " + self.size + ", Color : " + self.color + ", Moda : " + self.fashion

    class Meta:
        db_table = "Cloth"


class Cotizacion(models.Model):
    value_cloth = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    value_work = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    value_threads = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    value_buttons = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    value_necks = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=False)
    value_embroidery = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=False)
    value_prints = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=False)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE, blank=False, null=False)
    client = models.ManyToManyField(Client, through="CotizacionClient")
    #####################
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lookup_field = 'pk'

    class Meta:
        db_table = "Cotizacion"


class CotizacionClient(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    total = models.BigIntegerField()
    #####################
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lookup_field = 'pk'

    class Meta:
        db_table = "Cotizacion_Client"


class Alquiler(models.Model):
    date_now = models.DateField(auto_now_add=True)  # [YYYY-MM-DD]
    date_return = models.DateField()  # [YYYY-MM-DD]
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=5000.00)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE, blank=False, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    ifrental = models.SmallIntegerField(default=1, null=False, blank=False)
    #####################
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lookup_field = 'pk'

    def __str__(self):
        return str(self.date_now) + "" + str(self.date_return) + "" + str(self.price)

    class Meta:
        db_table = "Rental"
