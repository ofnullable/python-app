from marshmallow import fields

from bugbounty.utils import CamelCaseSchema


class RegisterUser(CamelCaseSchema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()


class RegisterHacker(RegisterUser):
    pass


class RegisterVendor(RegisterUser):
    vendor_name = fields.Str()
    vendor_info = fields.Str()


class UserProfile(CamelCaseSchema):
    image = fields.Str()
    score = fields.Int()


class VendorProfile(UserProfile):
    vendor_name = fields.Str()
    vendor_info = fields.Str()


class UserResponse(CamelCaseSchema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    is_vendor = fields.Bool()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()


class HackerResponse(UserResponse):
    profile = fields.Nested(UserProfile)


class VendorResponse(UserResponse):
    profile = fields.Nested(VendorProfile)


register_hacker = RegisterHacker()
hacker_response = HackerResponse()

register_vendor = RegisterVendor()
vendor_response = VendorResponse()
