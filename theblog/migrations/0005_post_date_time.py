# Generated by Django 3.1.5 on 2021-01-07 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
