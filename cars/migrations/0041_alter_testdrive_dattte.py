# Generated by Django 4.1.4 on 2023-03-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0040_featuredvechiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdrive',
            name='dattte',
            field=models.DateTimeField(default=None, null=True, verbose_name='Customer Perfer Time For Test Drive'),
        ),
    ]
