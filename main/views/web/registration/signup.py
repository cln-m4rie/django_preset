from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from main.forms import SignupForm


class SignupView(FormView):
    template_name = 'main/registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('main:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:index')

    def form_valid(self, form):
        user = form.create_user()
        if user is None:
            return super().form_invalid(form)
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response
