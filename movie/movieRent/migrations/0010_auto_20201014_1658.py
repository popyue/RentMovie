# Generated by Django 3.1.1 on 2020-10-14 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieRent', '0009_movieproduct_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(default='Fast Frious', max_length=20)),
                ('slug', models.SlugField(default=None, max_length=200)),
                ('movie_describe', models.TextField(max_length=1000)),
                ('movie_score', models.FloatField(default=10.0)),
                ('in_stock', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField(default=500.0)),
                ('picture', models.ImageField(null=True, upload_to='static/movie_pic/')),
                ('videofile', models.FileField(null=True, upload_to='static/videos/', verbose_name='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movieRent.category')),
            ],
            options={
                'ordering': ('movie_name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.DeleteModel(
            name='MovieProduct',
        ),
    ]