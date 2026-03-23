from django.contrib import admin

from users.models import ITSpecialistApplicant


@admin.register(ITSpecialistApplicant)
class ITSpecialistApplicantAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "desired_position",
        "phone_number",
        "city",
        "experience_years",
    )
    search_fields = ("username", "first_name", "last_name", "phone_number", "city")
