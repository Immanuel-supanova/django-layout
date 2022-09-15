from django.contrib.auth import get_user_model
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import RegisterForm

User = get_user_model()


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "auth/signup.html"

    def get_success_url(self, *args, **kwargs):  # use this to direct to its immediate detail view
        return reverse_lazy('home')


class HomeView(TemplateView):
    template_name = "index.html"
