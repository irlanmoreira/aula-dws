# Generated by Django 4.1.2 on 2022-12-22 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0018_question_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publications',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
