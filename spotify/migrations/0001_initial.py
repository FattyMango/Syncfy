# Generated by Django 3.1.3 on 2021-05-07 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('is_active_playback', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lobbyuser1', to=settings.AUTH_USER_MODEL)),
                ('users_connected', models.ManyToManyField(blank=True, related_name='users_conntected', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='current_song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_uri', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('lobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lobby', to='spotify.lobby')),
            ],
        ),
        migrations.CreateModel(
            name='Access_token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(blank=True, max_length=500, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=500, null=True)),
                ('expiers_at', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
