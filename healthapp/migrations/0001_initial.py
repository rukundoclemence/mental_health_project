# Generated by Django 5.0.1 on 2024-02-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]