from marshmallow import fields

from bugbounty.utils import CamelCaseSchema


class RegisterUser(CamelCaseSchema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    is_vendor = fields.Bool()


class UserResponse(CamelCaseSchema):
    username = fields.Str()
    email = fields.Email()
    image = fields.Url()
    is_vendor = fields.Bool()
    createdAt = fields.DateTime(attribute='created_at', dump_only=True)
    updatedAt = fields.DateTime(attribute='updated_at')


register_user = RegisterUser()
user_response = UserResponse()
