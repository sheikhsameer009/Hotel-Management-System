# Generated by Django 4.0.4 on 2022-05-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelweb', '0002_alter_paymentinfo_card_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email_address',
            field=models.CharField(blank=True, db_column='Email_Address', max_length=35, null=True),
        ),
    ]
