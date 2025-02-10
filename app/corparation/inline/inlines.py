from django.contrib.admin import StackedInline
from ..models import Building,PhoneNumber,FoodType,CarsType,OtherProductType#,Activities

# this is inline Building model 
class BuildingInline(StackedInline):
    model=Building
    extra=0
    readonly_fields=['latitude','longitude','created_at']

# this is inline PhoneNumber model
class PhoneNumberInline(StackedInline):
    model=PhoneNumber
    extra=0


class FoodTypeInline(StackedInline):
    model=FoodType
    extra=0

class CarsTypeInline(StackedInline):
    model=CarsType
    extra=0

class OtherProductTypeInline(StackedInline):
    model=OtherProductType
    extra=0

#class ActivitesInline(StackedInline):
#    model=Activities
#    extra=0