from django.db import models
import secrets
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


class Organazation(models.Model):
    title = models.CharField(_('title'), null=True, blank=True, max_length=280)
    token = models.CharField(_('token'), max_length=64, unique=True, blank=True)
    
    class Meta:
        verbose_name=_('Organazation')
        verbose_name_plural=_('Organazations')
    
    def save(self, *args, **kwargs):
        if not self.token:  # Generate a token only if it's not set
            self.token = secrets.token_hex(32)  # Generates a 64-character hex token
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

    
class PhoneNumber(models.Model):
    category=models.ForeignKey(Organazation,on_delete=models.CASCADE,verbose_name=_('category'))
    phone_number=models.CharField(_('phone_number'),max_length=20)
    created_at=models.DateTimeField(_('created_at'),default=timezone.now)
    class Meta:
        verbose_name=_('Phone Number')
        verbose_name_plural=_('Phone Numbers')
    
    def __str__(self):
        return f"{self.category.title} {_('Phone numbers')}"
    


class Building(models.Model):
    category = models.ForeignKey(Organazation, on_delete=models.CASCADE, verbose_name=_('category'))
    address = models.CharField(_('address'), max_length=280)
    latitude = models.FloatField(_('latitude'), null=True, blank=True)  # Fixed field name
    longitude = models.FloatField(_('longitude'), null=True, blank=True)  # Fixed field name
    created_at = models.DateTimeField(_('created_at'), default=timezone.now)

    class Meta:
        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')

    def __str__(self):
        return self.address

    def save(self, *args, **kwargs):
        if self.address and (self.latitude is None or self.longitude is None):  # Only fetch if missing
            geolocator = Nominatim(user_agent="my_geocoder")  # Set user_agent to avoid API blocking
            try:
                location = geolocator.geocode(self.address, timeout=10)
                if location:
                    self.latitude = location.latitude
                    self.longitude = location.longitude
            except GeocoderTimedOut:
                print("Geocoding service timed out")  # Handle timeout error

        super().save(*args, **kwargs)  # Call parent save method

#class BaseProductType(models.Model):
#   
#    created_at = models.DateTimeField(_('created_at'), default=timezone.now)
#
#    class Meta:
#        abstract = True  # Это абстрактная модель, она не создаст таблицу в БД
#
#    def __str__(self):
#        return self.title
#

class FoodType(models.Model):
    category = models.ForeignKey(Organazation, on_delete=models.CASCADE, related_name="food_types")
    title = models.CharField(_('title'), max_length=50)

    class Meta:
        verbose_name = _('Food Type')
        verbose_name_plural = _('Food Types')

class CarsType(models.Model):
    category = models.ForeignKey(Organazation, on_delete=models.CASCADE, related_name="car_types")
    title = models.CharField(_('title'), max_length=50)
    class Meta:
        verbose_name = _('Car Type')
        verbose_name_plural = _('Car Types')

class OtherProductType(models.Model):
    category = models.ForeignKey(Organazation, on_delete=models.CASCADE, related_name="other_product_types")
    title = models.CharField(_('title'), max_length=50)
    class Meta:
        verbose_name = _('Other Product Type')
        verbose_name_plural = _('Other Product Types')



#class Activities(models.Model):
#    category = models.ForeignKey(Organazation, on_delete=models.CASCADE, verbose_name=_('category'))
#    product_type = models.ForeignKey(BaseProductType, on_delete=models.CASCADE, verbose_name=_('product type'))
#    products=models.CharField(_('products'),max_length=200,choices=)
#    class Meta:
#        verbose_name = _('Activity')
#        verbose_name_plural = _('Activities')
    ## Динамическая связь с любой моделью ProductType
    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #object_id = models.PositiveIntegerField()
    #type_choice = GenericForeignKey('content_type', 'object_id')
#
    #class Meta:
    #    verbose_name = _('Activity')
    #    verbose_name_plural = _('Activities')
#
    #def __str__(self):
    #    return f"{self.category} - {self.type_choice}"





        



