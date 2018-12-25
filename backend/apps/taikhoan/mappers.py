from marshmallow import Schema, fields, post_load

from backend.apps.base.mappers import (
    PagingResponseSchema,
    PagingRequestSchema
)
from backend.apps.taikhoan.contracts import (
    GetTaiKhoanListRequest,
    PostTaiKhoanRequest,
    GetTaiKhoanRequest,
    PutTaiKhoanRequest,
    DeleteTaiKhoanRequest
)


class TaiKhoanResponseSchema(Schema):
    id = fields.Int()
    tendangnhap = fields.Str(required=True, allow_none=True)
    matkhau = fields.Str(required=True, allow_none=True)
    role_id = fields.Int(required=True, allow_none=True)


class GetTaiKhoanListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetTaiKhoanListRequest(**data)


class GetTaiKhoanListResponseSchema(PagingResponseSchema):
    results = fields.Nested(TaiKhoanResponseSchema, many=True, allow_none=True)


class PostTaiKhoanRequestSchema(Schema):
    tendangnhap = fields.Str(required=True, allow_none=True)
    matkhau = fields.Str(required=True, allow_none=True)
    role_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostTaiKhoanRequest(**data)


class GetTaiKhoanRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetTaiKhoanRequest(**data)


class PutTaiKhoanRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    tendangnhap = fields.Str(required=True, allow_none=True)
    matkhau = fields.Str(required=True, allow_none=True)
    role_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutTaiKhoanRequest(**data)


class DeleteTaiKhoanRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteTaiKhoanRequest(**data)
