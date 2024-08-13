# Generated by Django 4.2.5 on 2024-02-11 14:35

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Conversation",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(default="Mock title", max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="user", max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "conversation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="versions", to="chat.conversation"
                    ),
                ),
                (
                    "parent_version",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="chat.version"
                    ),
                ),
                (
                    "root_message",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="root_message_versions",
                        to="chat.message",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="message",
            name="role",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="chat.role"),
        ),
        migrations.AddField(
            model_name="message",
            name="version",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="messages", to="chat.version"
            ),
        ),
        migrations.AddField(
            model_name="conversation",
            name="active_version",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="current_version_conversations",
                to="chat.version",
            ),
        ),
        migrations.AddField(
            model_name="conversation",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
