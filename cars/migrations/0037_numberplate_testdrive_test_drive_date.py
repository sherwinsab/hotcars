# Generated by Django 4.1.4 on 2023-03-25 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0036_alter_testdrive_options_testdrive_test_drive_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='numberplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='testdrive',
            name='test_drive_date',
            field=models.DateField(null=True, verbose_name='Test Drive Date Customer Perfered'),
        ),
    ]

