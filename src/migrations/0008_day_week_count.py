# Generated by Django 3.1.2 on 2020-11-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0007_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='week_count',
            field=models.CharField(default='week count', max_length=20),
        ),
    ]