from django.db import models


# Create your models here.
from realtos.models import Realtor
from django.contrib.auth.models import User

class listings(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=150)
    desc = models.CharField(max_length=150, verbose_name='Description')
    price = models.IntegerField()
    badroom = models.IntegerField()
    garage = models.BooleanField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(decimal_places=2,max_digits=10)
    is_published = models.BooleanField()
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    list_date = models.DateTimeField(auto_now_add=False)
    update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-list_date',)

class Inquiry(models.Model):
    listing = models.ForeignKey(listings, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=150)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=False)
    update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('-timestamp',)
        verbose_name='Inquiry'
        verbose_name_plural='Inquires'