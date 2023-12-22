# Generated by Django 4.2.7 on 2023-12-22 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_productvariant_stock_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nba_player',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.nbaplayer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='team_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.team'),
        ),
    ]
