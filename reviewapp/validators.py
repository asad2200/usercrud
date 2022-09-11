import numpy as np
from django.core.exceptions import ValidationError

def rating_validator(value):
    """
        Validate ratings that value should be between 0 to 5
    """

    if not value in np.arange(0, 5.5, 0.5) :
        raise ValidationError("Rating should be between 0 and 5. ex: (0, 0.5, 1, 1.5 ...)")