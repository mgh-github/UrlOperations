# Generated by Django 3.1.1 on 2021-04-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrlApp', '0002_auto_20210418_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
    ]