from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('my-account')

class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        print("FILES:", self.request.FILES)
        print("AVATAR:", form.cleaned_data.get('avatar'))
        return super().form_valid(form)

    def form_invalid(self, form):
        print("FORM ERRORS:", form.errors)
        print("FILES:", self.request.FILES)
        return super().form_invalid(form)


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('my-account')