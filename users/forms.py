from django import forms
from django.contrib.auth.forms import UserCreationForm

from users import models


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    city = forms.CharField(max_length=120, required=True)
    gender = forms.ChoiceField(choices=models.ITSpecialistApplicant.GENDER, required=True)
    desired_position = forms.CharField(max_length=120, required=True, initial="IT Specialist")
    experience_years = forms.IntegerField(min_value=0, required=True)
    education = forms.CharField(widget=forms.Textarea, required=True)
    key_skills = forms.CharField(widget=forms.Textarea, required=True)
    expected_salary = forms.DecimalField(max_digits=12, decimal_places=2, required=True)
    english_level = forms.ChoiceField(
        choices=models.ITSpecialistApplicant.ENGLISH_LEVEL,
        required=True,
    )
    work_format = forms.ChoiceField(
        choices=models.ITSpecialistApplicant.WORK_FORMAT,
        required=True,
    )
    portfolio_url = forms.URLField(required=False)
    github_url = forms.URLField(required=False)

    class Meta:
        model = models.ITSpecialistApplicant
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "photo",
            "birth_date",
            "phone_number",
            "city",
            "gender",
            "desired_position",
            "experience_years",
            "education",
            "key_skills",
            "expected_salary",
            "english_level",
            "work_format",
            "portfolio_url",
            "github_url",
            "ready_to_relocate",
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
