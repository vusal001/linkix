# Generated by Django 4.0.4 on 2022-05-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_link_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='linktype',
            field=models.CharField(choices=[('Youtube videosu', 'Youtube videosu'), ('TikTok', 'TikTok'), ('Instagram', 'Instagram'), ('18+ kontent', '18+ kontent'), ('Oyun', 'Oyun'), ('Yükləmə linki', 'Yükləmə linki'), ('Film/Serial', 'Film/Serial'), ('Digər', 'Digər')], default=1, max_length=100, verbose_name='Linkin kategoriyası'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Post slug'),
        ),
    ]