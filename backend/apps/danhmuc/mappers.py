from marshmallow import Schema, fields, post_load

from backend.apps.base.mappers import (
    PagingResponseSchema,
    PagingRequestSchema
)
from backend.apps.danhmuc.contracts import (
    GetDanhMucListRequest,
    PostDanhMucRequest,
    GetDanhMucRequest,
    PutDanhMucRequest,
    DeleteDanhMucRequest,
)


class DanhMucResponseSchema(Schema):
    id = fields.Int()
    danhmuccha = fields.Int(required=True, allow_none=True)
    tendanhmuc = fields.Str(required=True, allow_none=True)
    link = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetDanhMucListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetDanhMucListRequest(**data)


class GetDanhMucListResponseSchema(PagingResponseSchema):
    results = fields.Nested(DanhMucResponseSchema, many=True, allow_none=True)


class PostDanhMucRequestSchema(Schema):
    danhmuccha = fields.Int(required=True, allow_none=True)
    tendanhmuc = fields.Str(required=True, allow_none=True)
    link = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostDanhMucRequest(**data)


class GetDanhMucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetDanhMucRequest(**data)


class PutDanhMucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    danhmuccha = fields.Int(required=True, allow_none=True)
    tendanhmuc = fields.Str(required=True, allow_none=True)
    link = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutDanhMucRequest(**data)


class DeleteDanhMucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteDanhMucRequest(**data)
