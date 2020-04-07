from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Category name')

    def __str__(self):
        return self.name


class Institution(models.Model):
    FOUNDATION = 'found'
    NON_GOVERNMENTAL_ORGANIZATION = 'non gov org'
    LOCAL_COLLECTION = 'loc org'
    TYPES = (
        (FOUNDATION, _('Foundation')),
        (NON_GOVERNMENTAL_ORGANIZATION, _('Non governmental organization')),
        (LOCAL_COLLECTION, _('Local collection'),),
    )

    name = models.CharField(max_length=140, verbose_name='Institution name')
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TYPES, default=FOUNDATION)
    categories = models.ManyToManyField('Category', related_name='institutions')

    def __str__(self):
        return f'{self.name} ({self.get_type_display()})'


class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField(verbose_name='Number of bags')
    categories = models.ManyToManyField('Category', related_name='donations')
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=150, verbose_name='Street and number')
    phone_number = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField(auto_now_add=True)
    pick_up_time = models.TimeField(auto_now_add=True)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Donation from user: {self.user} - {self.quantity} bag(s)'
