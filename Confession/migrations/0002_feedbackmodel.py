# Generated by Django 4.1.2 on 2022-11-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Confession', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedbackdetails', models.TextField()),
                ('feedbackprovider', models.CharField(max_length=20)),
            ],
        ),
    ]