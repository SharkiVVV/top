# Generated by Django 4.1.4 on 2023-05-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments_allowed',
            field=models.BooleanField(default=True),
        ),
    ]
