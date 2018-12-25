from marshmallow import Schema, fields, post_load

from backend.apps.base.mappers import (
    PagingResponseSchema,
    PagingRequestSchema
)
from backend.apps.tintuc.contracts import (
    GetTinTucListRequest,
    PostTinTucRequest,
    GetTinTucRequest,
    PutTinTucRequest,
    DeleteTinTucRequest,
)


class TinTucResponseSchema(Schema):
    id = fields.Int()
    danhmuc_id = fields.Int(required=True, allow_none=True)
    tieude = fields.Str(required=True, allow_none=True)
    hinhanh = fields.Str(required=True, allow_none=True)
    mota = fields.Str(required=True, allow_none=True)
    noidung = fields.Str(required=True, allow_none=True)
    ngaydang = fields.Date(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetTinTucListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetTinTucListRequest(**data)


class GetTinTucListResponseSchema(PagingResponseSchema):
    results = fields.Nested(TinTucResponseSchema, many=True, allow_none=True)


class PostTinTucRequestSchema(Schema):
    danhmuc_id = fields.Int(required=True, allow_none=True)
    tieude = fields.Str(required=True, allow_none=True)
    hinhanh = fields.Str(required=True, allow_none=True)
    mota = fields.Str(required=True, allow_none=True)
    noidung = fields.Str(required=True, allow_none=True)
    ngaydang = fields.Date(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostTinTucRequest(**data)


class GetTinTucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetTinTucRequest(**data)


class PutTinTucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    danhmuc_id = fields.Int(required=True, allow_none=True)
    tieude = fields.Str(required=True, allow_none=True)
    hinhanh = fields.Str(required=True, allow_none=True)
    mota = fields.Str(required=True, allow_none=True)
    noidung = fields.Str(required=True, allow_none=True)
    ngaydang = fields.Date(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutTinTucRequest(**data)


class DeleteTinTucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteTinTucRequest(**data)
