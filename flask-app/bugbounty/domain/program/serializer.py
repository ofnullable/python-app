from marshmallow import fields

from bugbounty.utils import CamelSchema


class ProgramPolicy(CamelSchema):
    id = fields.Int()
    contents = fields.Str()
    writer_id = fields.Int()
    program_id = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class ProgramResponse(CamelSchema):
    id = fields.Int()
    title = fields.Str()
    vendor_id = fields.Int()
    is_public = fields.Bool()
    is_proceeding = fields.Bool()
    policies = fields.List(fields.Nested(ProgramPolicy), attribute='policies')


class RegisterProgramPolicy(CamelSchema):
    contents = fields.Str(required=True)
    writer_id = fields.Int(required=True)
    program_id = fields.Int(required=True)


class UpdateProgram(CamelSchema):
    is_public = fields.Bool(required=True)
    is_proceeding = fields.Bool(required=True)


program_response = ProgramResponse()
programs_response = ProgramResponse(many=True)

register_program_policy = RegisterProgramPolicy()
