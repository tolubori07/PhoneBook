# Generated by Django 4.2.3 on 2023-08-14 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_contact_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contacts',
        ),
        migrations.AddField(
            model_name='user',
            name='contact_list',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.contact_list'),
        ),
    ]