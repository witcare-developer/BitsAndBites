# Generated by Django 4.1.7 on 2023-03-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0002_produto_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='nome',
            field=models.TextField(default=''),
        ),
    ]
