# Generated by Django 3.2.13 on 2022-06-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.PositiveIntegerField(blank=True)),
                ('message', models.TextField()),
            ],
        ),
    ]