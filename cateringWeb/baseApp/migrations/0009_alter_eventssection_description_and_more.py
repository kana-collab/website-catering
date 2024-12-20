# Generated by Django 5.1.4 on 2024-12-18 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0008_aboutsection_image1_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventssection',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Event Description'),
        ),
        migrations.AlterField(
            model_name='eventssection',
            name='image_description',
            field=models.CharField(default='default', max_length=200, verbose_name='Event Image description'),
        ),
    ]
