# Generated by Django 5.0 on 2023-12-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True)),
            ],
        ),
    ]
