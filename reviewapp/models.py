from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from .validators import rating_validator

User = get_user_model()

# Create your models here.

class Apartment(models.Model):
    """
        Apartment table - store apartment details
    """

    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name

class ApartmentReview(models.Model):
    """
        Apartment Review table - Store apartment review of users
        FK: apartment table, user table
    """

    apartment = models.ForeignKey(Apartment, models.CASCADE, related_name='apartment_review')
    user = models.ForeignKey(User, models.CASCADE, related_name='user_review')
    overall_rating = models.FloatField(_('Overall rating'), default=0.0, blank=True, null=True, validators=[rating_validator])
    cleanliness = models.FloatField(_('Cleanliness'), default=0.0, blank=True, null=True, validators=[rating_validator])
    communication = models.FloatField(_('Communication'), default=0.0, blank=True, null=True, validators=[rating_validator])
    check_in = models.FloatField(_('Check-in'), default=0.0, blank=True, null=True, validators=[rating_validator])
    accuracy = models.FloatField(_('Accuracy'), default=0.0, blank=True, null=True, validators=[rating_validator])
    location = models.FloatField(_('Location'), default=0.0, blank=True, null=True, validators=[rating_validator])
    value = models.FloatField(_('Value'), default=0.0, blank=True, null=True, validators=[rating_validator])
    review = models.TextField(_("Review"))

    class Meta:
        unique_together = ('apartment', 'user',)
    
    def __str__(self) -> str:
        return f" {self.user} user's review for {self.apartment}."
