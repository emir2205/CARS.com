from django.db import models

from cars_facts.models import Car


class DriverModel(models.Model):
    full_name = models.CharField(max_length=100, default='ФИО водителя')
    photo = models.ImageField(upload_to='drivers/')
    birth_date = models.DateField()
    choice_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driving_experience = models.PositiveIntegerField(default=1)
    driver_license = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.choice_car}"
