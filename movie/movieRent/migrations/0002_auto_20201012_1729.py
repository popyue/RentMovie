# Generated by Django 3.1.1 on 2020-10-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieRent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieproduct',
            old_name='categorye',
            new_name='category',
        ),
        migrations.AddField(
            model_name='movieproduct',
            name='pub_date',
            field=models.DateTimeField(default=None, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='movieproduct',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]