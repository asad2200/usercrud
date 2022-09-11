from django import forms
from . import models


class ApartmentReviewForm(forms.ModelForm):
    class Meta:
        model = models.ApartmentReview
        fields = "__all__"