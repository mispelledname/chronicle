# Generated by Django 3.2 on 2021-04-09 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oddjob', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='contributors',
            field=models.ManyToManyField(related_name='contributors', to='oddjob.User'),
        ),
        migrations.AlterField(
            model_name='job',
            name='originUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riginUser', to='oddjob.user'),
        ),
    ]