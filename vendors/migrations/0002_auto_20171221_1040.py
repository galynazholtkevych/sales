# Generated by Django 2.0 on 2017-12-21 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendors', to='common.Address'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
