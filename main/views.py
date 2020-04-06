from django.shortcuts import render
from django.views import View


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render(request, 'main/index.html')


class LoginPage(View):
    def get(self, request):
        return render(request, 'main/login.html')


class RegisterPage(View):
    def get(self, request):
        return render(request, 'main/register.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'main/add_donation.html')
