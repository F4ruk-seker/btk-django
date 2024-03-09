from django.contrib.auth import logout
from django.views.generic import FormView, RedirectView
from django.shortcuts import HttpResponseRedirect


class LoginView(FormView):
    ...


class RegisterView(FormView):
    ...


class LogoutView(RedirectView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
