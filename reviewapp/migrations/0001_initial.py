# Generated by Django 3.2.15 on 2022-09-11 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import reviewapp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_rating', models.FloatField(blank=True, default=0.0, null=True, validators=[reviewapp.validators.rating_validator], verbose_name='Overall rating')),
                ('cleanliness', models.FloatField(blank=True, default=0.0, null=True, validators=[reviewapp.validators.rating_validator], verbose_name='Cleanliness')),
                ('communication', models.FloatField(blank=True, default=0.0, null=True, validators=[reviewapp.validators.rating_validator], verbose_name='Communication')),
                ('check_in', models.FloatField(blank=True, default=0.0, null=True, validators=[reviewapp.validators.rating_validator], verbose_name='Check-in')),
                ('accuracy', models.FloatField(blank=True, default=0.0, null=True, validators=[reviewapp.validators.rating_validator], verbose_name='Accuracy')),
                ('location', models.FloatField(blank=True, default=0.0, null=True, validators=[reviewapp.validators.rating_validator], verbose_name='Location')),
                ('value', models.FloatField(blank=True, default=0.0, null=True, validators=[reviewapp.validators.rating_validator], verbose_name='Value')),
                ('review', models.TextField(verbose_name='Review')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment_review', to='reviewapp.apartment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('apartment', 'user')},
            },
        ),
    ]