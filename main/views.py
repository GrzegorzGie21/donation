from django.db.models import F, Sum, Count
from django.shortcuts import render
from django.views import View

from main.models import Donation, Institution


# Create your views here.
class LandingPage(View):
    def get(self, request):
        bags, institutions = self.get_bags_and_institutions()
        context = {'bags': bags.get('quantity_sum'),
                   'institutions': institutions,
                   'foundations': self.get_institutions_by_type('found'),
                   'non_gov_org': self.get_institutions_by_type('non gov org'),
                   'locals': self.get_institutions_by_type('loc org')
                   }
        return render(request, 'main/index.html', context)

    def get_bags_and_institutions(self):
        bags = Donation.objects.aggregate(Sum('quantity'))
        institutions = Institution.objects.all().count()
        return bags, institutions

    def get_institutions_by_type(self, type):
        # indtitution_types = Institution.objects.values_list('type', flat=True).distinct()
        # institutions_by_type = {}
        # for value in indtitution_types:
        #     institutions_by_type[value] = Institution.objects.filter(type=value)
        institutions_per_type = Institution.objects.filter(type=type)
        # institutions_per_type = Institution.objects.values('type').annotate(all_institutions=F('name'))
        return institutions_per_type

class LoginPage(View):
    def get(self, request):
        return render(request, 'main/login.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'main/add_donation.html')
