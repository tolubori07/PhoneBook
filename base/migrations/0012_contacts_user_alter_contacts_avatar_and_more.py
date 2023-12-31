# Generated by Django 4.2.3 on 2023-08-15 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_contact_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='avatar',
            field=models.ImageField(default='default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_contacts', to='base.contacts'),
        ),
        migrations.DeleteModel(
            name='Contact_list',
        ),
    ]
