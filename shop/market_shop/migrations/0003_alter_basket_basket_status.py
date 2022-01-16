# Generated by Django 3.2.9 on 2022-01-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_shop', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='basket_status',
            field=models.CharField(blank=True, choices=[('chk', 'check'), ('del', 'delete'), ('vrf', 'verify'), ('act', 'active')], default='chk', max_length=3, null=True),
        ),
    ]