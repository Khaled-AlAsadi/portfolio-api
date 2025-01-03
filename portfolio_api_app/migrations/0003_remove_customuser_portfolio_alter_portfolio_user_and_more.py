# Generated by Django 5.1.1 on 2024-12-15 22:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api_app', '0002_portfolio_customuser_portfolio_workexperince'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='portfolio',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workexperince',
            name='years',
            field=models.CharField(max_length=30),
        ),
    ]
