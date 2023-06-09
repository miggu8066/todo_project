# Generated by Django 4.1 on 2023-05-03 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0003_alter_user_options_alter_user_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Todo_list",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("todo_content", models.CharField(max_length=500)),
                (
                    "writer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.user",
                        verbose_name="작성자",
                    ),
                ),
            ],
            options={
                "verbose_name": "투두아이템",
                "verbose_name_plural": "투두아이템",
                "db_table": "todo_item",
            },
        ),
    ]
