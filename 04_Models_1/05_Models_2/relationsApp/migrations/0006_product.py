# Generated by Django 4.2.3 on 2023-07-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationsApp', '0005_alter_adress_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('account', models.ManyToManyField(to='relationsApp.account')),
            ],
        ),
    ]