# Generated by Django 4.1 on 2022-08-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_image_description_alter_image_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
