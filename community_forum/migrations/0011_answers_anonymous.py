# Generated by Django 3.1.5 on 2021-02-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_forum', '0010_questions_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
