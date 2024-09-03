# Generated by Django 5.0.4 on 2024-09-03 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
        ('store', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='accounts.vendor'),
        ),
    ]
