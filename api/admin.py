from django.contrib import admin
from api.models import Category, Dish, Review

# Register your models here.

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Review)
