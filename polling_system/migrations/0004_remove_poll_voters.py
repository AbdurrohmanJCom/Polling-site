# Generated by Django 4.2.7 on 2023-11-18 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling_system', '0003_candidate_votes_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='voters',
        ),
    ]