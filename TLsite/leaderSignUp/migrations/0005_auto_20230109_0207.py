# Generated by Django 3.2.16 on 2023-01-09 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderSignUp', '0004_alter_trailguideleader_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='')),
                ('event_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderSignUp.event')),
            ],
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]
