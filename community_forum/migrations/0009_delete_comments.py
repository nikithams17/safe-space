# Generated by Django 3.1.5 on 2021-01-13 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community_forum', '0008_remove_comments_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
