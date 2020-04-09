from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model

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
