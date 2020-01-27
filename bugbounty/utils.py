from marshmallow import Schema


def to_camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


class CamelCaseSchema(Schema):
    def on_bind_field(self, field_name, field_obj):
        print(field_name, field_obj)
        field_obj.data_key = to_camelcase(field_obj.data_key or field_name)
