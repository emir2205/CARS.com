from django.db import models


class Car(models.Model):
    title = models.CharField("Название", max_length=100)
    brand = models.CharField("Бренд", max_length=100)
    model_name = models.CharField("Модель", max_length=100)
    year = models.PositiveIntegerField("Год выпуска")
    country = models.CharField("Страна производства", max_length=100)
    body_type = models.CharField("Тип кузова", max_length=100)
    engine = models.CharField("Двигатель", max_length=100)
    horsepower = models.PositiveIntegerField("Лошадиные силы")
    color = models.CharField("Цвет", max_length=50)
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="cars/", blank=True, null=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)
   
    def __str__(self):
        return f"{self.brand} {self.model_name}"
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
