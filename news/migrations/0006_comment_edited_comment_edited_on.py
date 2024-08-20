# Generated by Django 4.2.15 on 2024-08-20 08:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited',
            field=models.CharField(choices=[('0', 'Unedited'), (1, 'Edited')], default=0, max_length=8),
        ),
        migrations.AddField(
            model_name='comment',
            name='edited_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]