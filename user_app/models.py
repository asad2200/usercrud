from django.db import models
from django.utils.translation import gettext as _

from .validators import validate_phone_number, validate_pincode

# Create your models here.


class UserModel(models.Model):
    """
    User model to save user data
    """

    profile_image = models.ImageField(_("Profile Image"), upload_to="profile-images/")
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(
        _("Phone No."), max_length=10, unique=True, validators=[validate_phone_number]
    )
    dob = models.DateField(_("Date Of Birth"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserAddress(models.Model):
    """
    User Address model to save user address data
    This is related with user table through OneToOne relation
    """

    user = models.OneToOneField(UserModel, related_name='user_address', on_delete=models.CASCADE, primary_key=True)
    address_1 = models.TextField(_("Address Line 1"))
    address_2 = models.TextField(_("Address Line 2"))
    city = models.CharField(_("City"), max_length=20)
    state = models.CharField(_("State"), max_length=20)
    country = models.CharField(_("Country"), max_length=20)
    pincode = models.CharField(
        _("Pincode"), max_length=6, validators=[validate_pincode]
    )

    def __str__(self):
        return f"{self.user.first_name} - Addr: {self.address_1}"
