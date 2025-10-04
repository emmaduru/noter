from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, EmailAuthenticationForm

User = get_user_model()

class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("note_list")  # or your home URL name
        return super().dispatch(request, *args, **kwargs)
    
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = EmailAuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("note_list")  # or your home URL name
        return super().dispatch(request, *args, **kwargs)

