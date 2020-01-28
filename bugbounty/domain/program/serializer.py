from marshmallow import fields

from bugbounty.utils import CamelCaseSchema


class ProgramPolicy(CamelCaseSchema):
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime()


class ProgramResponse(CamelCaseSchema):
    id = fields.Int()
    title = fields.Str()
    vendor_id = fields.Int()
    is_public = fields.Bool()
    is_proceeding = fields.Bool()


program_response = ProgramResponse()
programs_response = ProgramResponse(many=True)
