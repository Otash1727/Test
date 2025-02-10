from django.contrib import admin
from .models import *
from .inline.inlines import PhoneNumberInline,BuildingInline,OtherProductTypeInline,FoodTypeInline,CarsTypeInline


@admin.register(Organazation)
class OrganazationAdmin(admin.ModelAdmin):
    list_display=['title','token']
    readonly_fields=['token']
    inlines=[PhoneNumberInline,BuildingInline,FoodTypeInline,OtherProductTypeInline,CarsTypeInline]



    

