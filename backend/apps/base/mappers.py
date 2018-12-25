from marshmallow import Schema, fields


class PagingRequestSchema(Schema):
    limit = fields.Int(allow_none=True)
    offset = fields.Int(allow_none=True)
    sort = fields.Str(allow_none=True)


class PagingResponseSchema(Schema):
    count = fields.Int(allow_none=True)
    current = fields.Str(allow_none=True)
    prev = fields.Str(allow_none=True)
    next = fields.Str(allow_none=True)


class NoContentResponseSchema(Schema):
    pass
