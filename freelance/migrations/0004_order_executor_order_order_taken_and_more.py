# Generated by Django 5.0.3 on 2024-04-02 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0003_remove_customer_rating_remove_executor_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executors', to='freelance.executor', verbose_name='Исполнитель'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_taken',
            field=models.BooleanField(default=False, verbose_name='Заказ сделан'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_taken_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время принятия заказа'),
        ),
    ]
