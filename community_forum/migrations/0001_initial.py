# Generated by Django 3.0.7 on 2020-11-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('category_name', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
