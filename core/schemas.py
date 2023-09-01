from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str()
    email = fields.Email()
    phone_number = fields.Str()
    name = fields.Str()
    created_at = fields.DateTime()


class DNAKitOrderSchema(Schema):
    id = fields.Str()
    sequencing_type = fields.Str()
    user = fields.Nested(UserSchema)
    shipping_info = fields.Dict()
    created_at = fields.DateTime()
