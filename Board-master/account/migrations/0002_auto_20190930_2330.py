# Generated by Django 2.2.5 on 2019-09-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='user_email'),
        ),
    ]
