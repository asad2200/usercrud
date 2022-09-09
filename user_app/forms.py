from django import forms
from . import models


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserModel
        fields = "__all__"


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = models.UserAddress
        fields = "__all__"
        exclude = [
            "user",
        ]
