# Generated by Django 5.0.4 on 2024-09-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='business_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
