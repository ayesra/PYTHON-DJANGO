# Generated by Django 4.2.3 on 2023-07-24 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationsApp', '0004_alter_adress_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='relationsApp.account'),
        ),
    ]
