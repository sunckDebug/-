# Generated by Django 3.0.5 on 2020-04-07 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='用户名称')),
                ('score', models.IntegerField(verbose_name='最新分数')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
        ),
    ]
