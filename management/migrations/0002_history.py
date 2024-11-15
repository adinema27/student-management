# Generated by Django 5.1.1 on 2024-10-25 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
