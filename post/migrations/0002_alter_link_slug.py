# Generated by Django 4.0.4 on 2022-05-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Post slug'),
        ),
    ]