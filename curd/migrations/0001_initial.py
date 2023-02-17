# Generated by Django 4.1.2 on 2023-02-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_Employee',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact_no', models.IntegerField(unique=True)),
                ('gender', models.CharField(max_length=500)),
                ('deginations', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=500)),
            ],
        ),
    ]
