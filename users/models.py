from django.contrib.auth.models import User
from django.db import models


class ITSpecialistApplicant(User):
    GENDER = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
    )

    ENGLISH_LEVEL = (
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIATE", "INTERMEDIATE"),
        ("ADVANCED", "ADVANCED"),
    )

    WORK_FORMAT = (
        ("OFFICE", "OFFICE"),
        ("REMOTE", "REMOTE"),
        ("HYBRID", "HYBRID"),
    )

    photo = models.ImageField(upload_to="it_applicants/")
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=120)
    gender = models.CharField(max_length=10, choices=GENDER, default="MALE")
    desired_position = models.CharField(max_length=120, default="IT Specialist")
    experience_years = models.PositiveIntegerField(default=0)
    education = models.TextField()
    key_skills = models.TextField()
    expected_salary = models.DecimalField(max_digits=12, decimal_places=2)
    english_level = models.CharField(
        max_length=20,
        choices=ENGLISH_LEVEL,
        default="BEGINNER",
    )
    work_format = models.CharField(
        max_length=20,
        choices=WORK_FORMAT,
        default="OFFICE",
    )
    portfolio_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    ready_to_relocate = models.BooleanField(default=False)

    def __str__(self):
        return self.username
