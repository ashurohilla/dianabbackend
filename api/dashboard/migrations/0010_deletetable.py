# Generated by Django 3.2.19 on 2024-02-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_rename_name_desktopfile_desktopfile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='deletetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('localtime', models.CharField(default=False, max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
