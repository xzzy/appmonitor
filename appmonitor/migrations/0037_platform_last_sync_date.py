# Generated by Django 3.2.23 on 2024-01-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmonitor', '0036_responsiblegroupoutstandingadvisoryemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='last_sync_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]