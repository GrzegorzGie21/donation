from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.views.generic import DetailView

from main.models import Donation

User = get_user_model()


class RegisterPage(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        first_name = request.POST.get('name')
        last_name = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
        print(type(User))
        return redirect('login')


class UserDetailView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
