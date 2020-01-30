from marshmallow import fields

from bugbounty.utils import CamelCaseSchema


class ProgramPolicy(CamelCaseSchema):
    id = fields.Int()
    contents = fields.Str()
    writer_id = fields.Int()
    program_id = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class ProgramResponse(CamelCaseSchema):
    id = fields.Int()
    title = fields.Str()
    vendor_id = fields.Int()
    is_public = fields.Bool()
    is_proceeding = fields.Bool()
    program_policy = fields.List(fields.Nested(ProgramPolicy), attribute='policy')


class RegisterProgramPolicy(CamelCaseSchema):
    contents = fields.Str()
    writer_id = fields.Int()
    program_id = fields.Int()


program_response = ProgramResponse()
programs_response = ProgramResponse(many=True)

register_program_policy = RegisterProgramPolicy()
