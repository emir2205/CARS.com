from django.contrib import admin

from cars_facts.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model_name', 'year', 'price', 'views')
    search_fields = ('title', 'brand', 'model_name')
