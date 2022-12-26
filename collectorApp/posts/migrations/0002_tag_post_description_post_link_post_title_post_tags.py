# Generated by Django 4.1.3 on 2022-12-26 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="description",
            field=models.TextField(default="Enter a description here"),
        ),
        migrations.AddField(
            model_name="post",
            name="link",
            field=models.URLField(default="http://example.com", null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="posts.tag"),
        ),
    ]