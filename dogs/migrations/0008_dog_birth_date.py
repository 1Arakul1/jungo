# Generated by Django 4.2.12 on 2025-04-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0007_alter_dog_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
