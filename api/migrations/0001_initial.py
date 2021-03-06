# Generated by Django 3.1.1 on 2020-09-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('company_name', models.CharField(max_length=80)),
                ('age', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('zip', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('web', models.URLField(max_length=255)),
            ],
        ),
    ]
