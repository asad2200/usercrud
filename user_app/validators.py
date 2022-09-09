from django.core.exceptions import ValidationError


def validate_phone_number(value):
    """
        Validate phonenumber length(10) and check it is in digit or not
    """

    if len(value) != 10:
        raise ValidationError("Phone number length should be 10 digits.")

    if not value.isdigit():
        raise ValidationError("Phone number should contains only numbers.")

def validate_pincode(value):
    """
        Validate pinocode length(6) and check it is in digit or not
    """

    if len(value) != 6:
        raise ValidationError("Pincode length should be 6 digits.")

    if not value.isdigit():
        raise ValidationError("Pincode should contains only numbers.")

