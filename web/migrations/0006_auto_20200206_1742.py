# Generated by Django 3.0.1 on 2020-02-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200206_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_typel',
            field=models.CharField(choices=[('new', 'new'), ('分享', 'share'), ('資訊', 'info'), ('練習', 'practice'), ('問題', 'problem'), ('其他', 'other')], default='new', max_length=30),
        ),
    ]
