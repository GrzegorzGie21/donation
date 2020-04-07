# Generated by Django 2.2 on 2020-04-06 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Institution name')),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('found', 'Foundation'), ('non gov org', 'Non governmental organization'), ('loc org', 'Local collection')], default='found', max_length=50)),
                ('categories', models.ManyToManyField(related_name='institutions', to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Number of bags')),
                ('address', models.CharField(max_length=150, verbose_name='Street and number')),
                ('phone_number', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=6)),
                ('pick_up_date', models.DateField(auto_now_add=True)),
                ('pick_up_time', models.TimeField(auto_now_add=True)),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(related_name='donations', to='main.Category')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Institution')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]