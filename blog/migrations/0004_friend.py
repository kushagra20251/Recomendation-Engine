# Generated by Django 2.2.9 on 2020-04-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='friend',
            fields=[
                ('friend_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('friend_username', models.CharField(max_length=100)),
            ],
        ),
    ]