# Generated by Django 4.0.4 on 2022-05-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateField(),
        ),
    ]
