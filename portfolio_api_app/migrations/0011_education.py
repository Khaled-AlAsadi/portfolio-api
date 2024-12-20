# Generated by Django 5.1.1 on 2024-12-18 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api_app', '0010_rename_tags_tag_work_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('school_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='portfolio_api_app.portfolio')),
            ],
        ),
    ]
