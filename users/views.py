from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from users import forms


class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = forms.CustomRegisterForm
    success_url = '/login/'


class AuthLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        captcha_answer = self.request.POST.get('captcha_answer')
        if captcha_answer != '7':
            form.add_error(None, 'Неверная CAPTCHA')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return '/congratulation/'


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class CongView(generic.TemplateView):
    template_name = 'cong.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
