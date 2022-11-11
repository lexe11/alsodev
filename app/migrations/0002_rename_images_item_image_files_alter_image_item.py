# Generated by Django 4.1.3 on 2022-11-11 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='images',
            new_name='image_files',
        ),
        migrations.AlterField(
            model_name='image',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.item'),
        ),
    ]