# Generated by Django 5.2.3 on 2025-06-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='use_code_highlighting',
            field=models.BooleanField(default=False),
        ),
    ]
