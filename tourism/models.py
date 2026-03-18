from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, default="Категория тура")

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=100, default="Название тура")
    description = models.TextField(default="Описание тура")
    location = models.CharField(max_length=100, default="Место тура")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duration = models.PositiveIntegerField(default=1)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {', '.join([i.name for i in self.tags.all()])}"


class Tourist(models.Model):
    full_name = models.CharField(max_length=100, default="ФИО")
    phone_number = models.CharField(max_length=20, default="+996")
    email = models.EmailField(default="почта")

    def __str__(self):
        return self.full_name


class TourBooking(models.Model):
    tourist = models.OneToOneField("Tourist", on_delete=models.CASCADE)
    tour = models.ForeignKey("Tour", on_delete=models.CASCADE)
    booking_date = models.DateField()
    people_count = models.PositiveIntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tourist} - {self.tour}"


class TourReview(models.Model):
    tour = models.ForeignKey("Tour", on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, default="Имя автора")
    text = models.TextField(default="Отзыв о туре")
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tour} - {self.text}"
