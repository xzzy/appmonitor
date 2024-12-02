# Generated by Django 5.0.9 on 2024-11-29 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmonitor', '0054_platform_git_repo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PythonDependaBotAdvisory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('ecosystem', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('severity', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('cve_id', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appmonitor.platform')),
            ],
        ),
    ]