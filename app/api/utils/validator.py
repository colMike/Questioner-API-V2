import re
from marshmallow import ValidationError
from datetime import datetime


def required(value):
    """Validate that field under validation does not contain null value"""

    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('This parameter cannot be null')
        return value


def email(email):
    """ Validate email format """

    if not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email):
        raise ValidationError('Invalid email format')

    return email


def password(password):
    """ Validate password is Strong """

    message = 'Invalid password'

    if len(password) < 8:
        raise ValidationError(message)

    scores = {}

    for letter in password:
        if letter.islower():
            scores['has_lower'] = 1

        if letter.isupper():
            scores['has_upper'] = 1

        if letter.isdigit():
            scores['has_digit'] = 1

    if sum(scores.values()) < 3:
        raise ValidationError(message)


def date(date):
    """ Function to validate meetup date """

    if not re.match(r"^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/([12][0-9]{3})$", date):
        raise ValidationError('Date should be in the format dd/mm/yyyy')

    date_format = "%d/%m/%Y"
    date = datetime.strptime(date, date_format)
    now = datetime.now()

    if date < now:
        raise ValidationError('Date should be in the future')


def tags(tags):
    """ Validate meetup tags are present """

    if not tags and not len(tags) > 0:
        raise ValidationError('You need to pass atleast 1 tag for the meetup')
