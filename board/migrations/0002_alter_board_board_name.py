# Generated by Django 4.1 on 2023-04-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="board_name",
            field=models.CharField(default="1번", max_length=32, verbose_name="게시판 종류"),
        ),
    ]