# Generated by Django 2.0.3 on 2018-03-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0041_auto_20180331_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='img/'),
        ),
    ]
