from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View

from main.models import Donation, Institution, Category


# Create your views here.
class LandingPage(View):
    def get(self, request):
        bags, institutions = self.get_bags_and_institutions()
        context = {'bags': bags.get('quantity__sum'),
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

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing-page')
        else:
            return redirect('register')


class LogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class AddDonationView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        context = {'categories': self.get_all_model_instances(Category, 'name'),
                   'institutions': self.get_all_model_instances(Institution)}
        return render(request, 'main/add_donation.html', context)

    def get_all_model_instances(self, model, order=None):
        if order:
            model_instances = model.objects.order_by(order)
        else:
            model_instances = model.objects.all()
        return model_instances

    def post(self, request):
        kwargs = {
            'categories': [category for category in request.POST['categories']],
            'quantity': request.POST['bags'],
            'organization': request.POST['organization'],
            'address': request.POST['address'],
            'city': request.POST['city'],
            'postcode': request.POST['postcode'],
            'phone': request.POST['phone'],
            'data': request.POST['data'],
            'time': request.POST['time'],
            'more_info': request.POST['more_info'],
            'user': request.user
        }
        print(kwargs)
        Donation.objects.create(**kwargs)
        return redirect('landing-page')


class ConfirmDonationView(View):
    def get(self, request):
        return render(request, 'main/form-confirmation.html')