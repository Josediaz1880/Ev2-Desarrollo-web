# Generated by Django 3.2.16 on 2023-06-11 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0007_auto_20230531_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucionmercancia',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.productos'),
        ),
        migrations.AddField(
            model_name='entradamercancia',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.productos'),
        ),
        migrations.AddField(
            model_name='salidamercancia',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.productos'),
        ),
    ]
