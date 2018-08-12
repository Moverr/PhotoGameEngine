# Generated by Django 2.1 on 2018-08-12 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import photogame.utils.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
                ('description', models.TextField(verbose_name='description')),
                ('category', models.CharField(choices=[(photogame.utils.enums.Categories('People'), 'People'), (photogame.utils.enums.Categories('Nature'), 'Nature'), (photogame.utils.enums.Categories('City Life'), 'City Life'), (photogame.utils.enums.Categories('Love'), 'Love'), (photogame.utils.enums.Categories('Sports'), 'Sports'), (photogame.utils.enums.Categories('Family'), 'Family')], max_length=255)),
                ('datecreated', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('votetype', models.CharField(choices=[(photogame.utils.enums.VoteTypes(1), 1), (photogame.utils.enums.VoteTypes(0), 0)], max_length=255)),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photogame.Picture')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]