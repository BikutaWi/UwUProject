# Generated by Django 3.2.12 on 2022-03-07 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uwuapp', '0008_auto_20220307_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
