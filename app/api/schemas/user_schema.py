from marshmallow import Schema, fields
from ..utils.validator import required, email, password


class UserSchema(Schema):
    """Schema for Users """

    id = fields.Integer(dump_only=True)
    firstname = fields.Str(required=True, validate=(required))
    lastname = fields.Str(required=True, validate=(required))
    username = fields.Str(required=True, validate=(required))
    othername = fields.Str(required=False)
    phonenumber = fields.Str(required=False)
    email = fields.Email(required=True, validate=(email))
    othername = fields.Str(required=False)
    password = fields.Str(required=True, validate=(required, password))
    registered = fields.DateTime(dump_only=True)
    questions_asked = fields.Int(dump_only=True)
    questions_commented = fields.Int(dump_only=True)
