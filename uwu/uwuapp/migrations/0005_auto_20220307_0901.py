# Generated by Django 3.2.12 on 2022-03-07 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uwuapp', '0004_alter_chapter_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='chapter_nb',
        ),
        migrations.CreateModel(
            name='IsFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uwuapp.manga')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]