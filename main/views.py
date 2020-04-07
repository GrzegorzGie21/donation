from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from main.models import Donation, Institution


# Create your views here.
class LandingPage(View):
    def get(self, request):
        bags, institutions = self.get_bags_and_institutions()
        context = {'bags': bags.get('quantity_sum'), 'institutions': institutions}
        return render(request, 'main/index.html', context)

    def get_bags_and_institutions(self):
        bags = Donation.objects.aggregate(Sum('quantity'))
        institutions = Institution.objects.all().count()
        return bags, institutions


class LoginPage(View):
    def get(self, request):
        return render(request, 'main/login.html')


class RegisterPage(View):
    def get(self, request):
        return render(request, 'main/register.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'main/add_donation.html')
