# Generated by Django 5.0.6 on 2024-07-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
