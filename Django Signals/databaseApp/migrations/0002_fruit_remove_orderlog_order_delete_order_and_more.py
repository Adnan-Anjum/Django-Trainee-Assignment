# Generated by Django 4.2.3 on 2024-10-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderlog',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderLog',
        ),
    ]
