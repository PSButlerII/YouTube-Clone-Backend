# Generated by Django 3.1.8 on 2021-07-22 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20210722_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='previous_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.comment'),
        ),
    ]
