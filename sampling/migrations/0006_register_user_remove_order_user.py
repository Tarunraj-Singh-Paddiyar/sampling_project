# Generated by Django 4.2.10 on 2024-02-27 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampling', '0005_alter_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
