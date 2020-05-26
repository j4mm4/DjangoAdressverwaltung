# Generated by Django 3.0.2 on 2020-05-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('housenumber', models.IntegerField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('zipCode', models.IntegerField(max_length=15)),
                ('phone', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
            ],
        ),
    ]