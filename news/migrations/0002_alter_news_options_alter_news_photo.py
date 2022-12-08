# Generated by Django 4.1.3 on 2022-11-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_at'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]