from marshmallow import fields

from bugbounty.utils import CamelSchema


class RegisterUser(CamelSchema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class RegisterHacker(RegisterUser):
    pass


class RegisterVendor(RegisterUser):
    vendor_name = fields.Str()
    vendor_info = fields.Str()


class UserProfile(CamelSchema):
    image = fields.Str()
    score = fields.Int()


class VendorProfile(UserProfile):
    vendor_name = fields.Str(required=True)
    vendor_info = fields.Str(required=False)


class UserResponse(CamelSchema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    is_vendor = fields.Bool()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class HackerResponse(UserResponse):
    profile = fields.Nested(UserProfile)


class VendorResponse(UserResponse):
    profile = fields.Nested(VendorProfile)


register_hacker = RegisterHacker()
hacker_response = HackerResponse()

register_vendor = RegisterVendor()
vendor_response = VendorResponse()
