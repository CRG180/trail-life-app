# Generated by Django 3.2.16 on 2023-01-09 00:13

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderSignUp', '0003_auto_20221229_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailguideleader',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
    ]
