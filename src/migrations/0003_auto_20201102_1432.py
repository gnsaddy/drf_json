# Generated by Django 3.1.2 on 2020-11-02 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20201102_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subContent', models.CharField(max_length=1000)),
                ('duration', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('coordinator', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.AddField(
            model_name='content',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.course'),
        ),
    ]
