# Generated by Django 2.0.3 on 2018-03-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newlib', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='available',
        ),
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
