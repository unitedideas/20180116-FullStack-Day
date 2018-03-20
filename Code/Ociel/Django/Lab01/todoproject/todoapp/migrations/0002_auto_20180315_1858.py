# Generated by Django 2.0.3 on 2018-03-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('notes', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]