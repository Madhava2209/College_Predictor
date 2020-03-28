# Generated by Django 3.0.3 on 2020-03-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_Name', models.CharField(max_length=100)),
                ('College_ID', models.CharField(max_length=10)),
                ('Location', models.CharField(max_length=100)),
                ('Rank', models.BigIntegerField()),
                ('Category', models.CharField(max_length=20)),
                ('Branch', models.CharField(max_length=100)),
            ],
        ),
    ]
