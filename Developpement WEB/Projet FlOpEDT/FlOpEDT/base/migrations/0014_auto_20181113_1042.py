# Generated by Django 2.1.2 on 2018-11-13 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_coursetype_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakingnews',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
        migrations.AddField(
            model_name='tutorcost',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
    ]