# Generated by Django 3.1.7 on 2021-06-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210622_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='RUC',
            field=models.CharField(default='Ingresar RUC, en caso Factura', max_length=11),
            preserve_default=False,
        ),
    ]
