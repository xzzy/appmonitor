# Generated by Django 3.2.19 on 2023-06-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmonitor', '0007_rename_manualchecks_manualcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualcheck',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='manualcheck',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]