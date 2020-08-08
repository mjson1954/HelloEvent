# Generated by Django 3.0.9 on 2020-08-08 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True)),
                ('time', models.DateTimeField(blank=True)),
                ('genre', models.CharField(choices=[('Busking', '버스킹'), ('Flee', '플리마켓'), ('Exihibit', '전시')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event_images', verbose_name='이벤트 이미지')),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
    ]