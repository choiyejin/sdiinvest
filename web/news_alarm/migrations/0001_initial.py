# Generated by Django 5.0.4 on 2024-04-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('souce', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
    ]
