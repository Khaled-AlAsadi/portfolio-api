# Generated by Django 5.1.1 on 2024-12-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api_app', '0011_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='date',
            field=models.CharField(default='', max_length=30),
        ),
    ]
