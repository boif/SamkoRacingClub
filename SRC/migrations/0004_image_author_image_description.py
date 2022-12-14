# Generated by Django 4.1.3 on 2023-01-05 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SRC', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=300, null=True, verbose_name='Description'),
        ),
    ]
