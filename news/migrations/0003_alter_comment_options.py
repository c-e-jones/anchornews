# Generated by Django 4.2.15 on 2024-08-13 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_author_alter_post_byline_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
    ]