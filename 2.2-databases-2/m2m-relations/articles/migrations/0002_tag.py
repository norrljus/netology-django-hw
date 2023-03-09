# Generated by Django 4.1.2 on 2023-02-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('is_main', models.BooleanField()),
                ('articles', models.ManyToManyField(related_name='scopes', to='articles.article')),
            ],
        ),
    ]