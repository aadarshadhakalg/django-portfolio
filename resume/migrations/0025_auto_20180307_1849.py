# Generated by Django 2.0.2 on 2018-03-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0024_auto_20180307_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.TextField(),
        ),
    ]
