# Generated by Django 3.1.8 on 2021-07-22 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='previous_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.comment'),
        ),
    ]
