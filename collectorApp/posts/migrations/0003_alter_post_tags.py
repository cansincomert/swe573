# Generated by Django 4.1.3 on 2022-12-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_tag_post_description_post_link_post_title_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(related_name="posts", to="posts.tag"),
        ),
    ]
