# Generated by Django 3.2.18 on 2023-07-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmonitor', '0009_notificationemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='json_key',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='check_operator',
            field=models.IntegerField(blank=True, choices=[(1, 'Positive Integer'), (2, 'Negative Integer'), (3, 'Equal Integer'), (4, 'Equal String')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='mon_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Web Page'), (2, 'Ping'), (3, 'Port Open'), (5, 'SSL Valid'), (6, 'Network Latency'), (7, 'Packet Loss'), (8, 'JSON Key')], default=1, null=True),
        ),
    ]
