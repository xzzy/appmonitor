# Generated by Django 3.2.18 on 2023-07-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmonitor', '0012_auto_20230728_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='down',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='monitor',
            name='up',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='monitor',
            name='warn',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]