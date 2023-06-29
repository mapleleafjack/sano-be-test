from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str()
    email = fields.Email()
    phone_number = fields.Str()
    name = fields.Str()
    created_at = fields.DateTime()
