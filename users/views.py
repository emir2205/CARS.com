from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from users import forms


def register_view(request):
    if request.method == "POST":
        form = forms.CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = forms.CustomRegisterForm()
    return render(request, "register.html", {"form": form})


def auth_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            captcha_answer = request.POST.get("captcha_answer")
            if captcha_answer == "7":
                user = form.get_user()
                login(request, user)
                return redirect("/congratulation/")
            form.add_error(None, "Неверная CAPTCHA")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/login/")


def cong_view(request):
    if request.method == "GET":
        user = User.objects.all()
    return render(
        request,
        "cong.html",
        {
            "user": user
        }
    )
