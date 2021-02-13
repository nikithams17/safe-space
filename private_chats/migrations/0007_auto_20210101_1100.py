# Generated by Django 3.0.7 on 2021-01-01 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_chats', '0006_groupchatroom_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='groupchatroom',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='groupchatroom',
            name='members',
        ),
        migrations.RemoveField(
            model_name='groupmessages',
            name='room',
        ),
        migrations.RemoveField(
            model_name='groupmessages',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='personalchatroom',
            name='msg_receiver',
        ),
        migrations.RemoveField(
            model_name='personalchatroom',
            name='msg_sender',
        ),
        migrations.RemoveField(
            model_name='personalmessages',
            name='chatroom',
        ),
        migrations.DeleteModel(
            name='FriendList',
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
        migrations.DeleteModel(
            name='GroupChatroom',
        ),
        migrations.DeleteModel(
            name='GroupMessages',
        ),
        migrations.DeleteModel(
            name='PersonalChatroom',
        ),
        migrations.DeleteModel(
            name='PersonalMessages',
        ),
    ]
