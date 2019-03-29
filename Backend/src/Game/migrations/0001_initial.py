# Generated by Django 2.1.7 on 2019-03-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_no', models.IntegerField()),
                ('row_no', models.IntegerField()),
                ('is_mine', models.BooleanField(default=True)),
                ('is_revealed', models.BooleanField(default=False)),
                ('is_flagged', models.BooleanField(default=False)),
                ('neighbour_mine_count', models.IntegerField()),
            ],
        ),
    ]