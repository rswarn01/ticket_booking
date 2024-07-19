# Generated by Django 4.2 on 2024-07-19 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bus_service_provider', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookinghistory',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_service_provider.booking'),
        ),
        migrations.AddField(
            model_name='bookinghistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blockhistory',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_service_provider.bus'),
        ),
        migrations.AddField(
            model_name='blockhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]