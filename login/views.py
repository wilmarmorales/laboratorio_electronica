from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


class LoginFormView(LoginView):
    template_name = 'login/login.html'


def logout_view(request):
    logout(request)
    return redirect('login:login')
