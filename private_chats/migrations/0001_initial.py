# Generated by Django 3.0.7 on 2020-12-10 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalChatroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('msg_receiver', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg_receiver', to='accounts.Profile')),
                ('msg_sender', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg_sender', to='accounts.Profile')),
            ],
            options={
                'verbose_name_plural': 'Personal Chatroom',
            },
        ),
        migrations.CreateModel(
            name='PersonalMessages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('message', models.TextField(max_length=2000)),
                ('chatroom', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_messages', to='private_chats.PersonalChatroom')),
            ],
            options={
                'verbose_name_plural': 'Personal messages',
            },
        ),
    ]