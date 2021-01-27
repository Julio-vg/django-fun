# Generated by Django 3.1.5 on 2021-01-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_article_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to='example.Publication'),
        ),
    ]
