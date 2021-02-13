# Generated by Django 3.0.7 on 2020-11-18 07:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answers_from_therapist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('answer', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Answers from therapist',
            },
        ),
        migrations.CreateModel(
            name='question_to_therapist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('question', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Questions for therapists',
            },
        ),
    ]