from marshmallow import Schema, fields, post_load

from backend.apps.base.mappers import (
    PagingResponseSchema,
    PagingRequestSchema
)
from backend.apps.dathang.contracts import (
    GetKhachHangListRequest,
    PostKhachHangRequest,
    GetKhachHangRequest,
    PutKhachHangRequest,
    DeleteKhachHangRequest,

    GetDonHangListRequest,
    PostDonHangRequest,
    GetDonHangRequest,
    PutDonHangRequest,
    DeleteDonHangRequest,

    GetCTDonHangListRequest,
    PostCTDonHangRequest,
    GetCTDonHangRequest,
    PutCTDonHangRequest,
    DeleteCTDonHangRequest
)


class KhachHangResponseSchema(Schema):
    id = fields.Int()
    tenkhachhang = fields.Str(required=True, allow_none=True)
    diachi = fields.Str(required=True, allow_none=True)
    email = fields.Str(required=True, allow_none=True)
    sdt = fields.Int(required=True, allow_none=True)


class GetKhachHangListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetKhachHangListRequest(**data)


class GetKhachHangListResponseSchema(PagingResponseSchema):
    results = fields.Nested(KhachHangResponseSchema, many=True, allow_none=True)


class PostKhachHangRequestSchema(Schema):
    tenkhachhang = fields.Str(required=True, allow_none=True)
    diachi = fields.Str(required=True, allow_none=True)
    email = fields.Str(required=True, allow_none=True)
    sdt = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostKhachHangRequest(**data)


class GetKhachHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetKhachHangRequest(**data)


class PutKhachHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    tenkhachhang = fields.Str(required=True, allow_none=True)
    diachi = fields.Str(required=True, allow_none=True)
    email = fields.Str(required=True, allow_none=True)
    sdt = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutKhachHangRequest(**data)


class DeleteKhachHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteKhachHangRequest(**data)


class DonHangResponseSchema(Schema):
    id = fields.Int()
    khachhang_id = fields.Int(required=True, allow_none=True)
    ngaydat = fields.Date(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetDonHangListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetDonHangListRequest(**data)


class GetDonHangListResponseSchema(PagingResponseSchema):
    results = fields.Nested(DonHangResponseSchema, many=True, allow_none=True)


class PostDonHangRequestSchema(Schema):
    khachhang_id = fields.Int(required=True, allow_none=True)
    ngaydat = fields.Date(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostDonHangRequest(**data)


class GetDonHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetDonHangRequest(**data)


class PutDonHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    khachhang_id = fields.Int(required=True, allow_none=True)
    ngaydat = fields.Date(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutDonHangRequest(**data)


class DeleteDonHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteDonHangRequest(**data)


class CTDonHangResponseSchema(Schema):
    id = fields.Int()
    donhang_id = fields.Int(required=True, allow_none=True)
    sanpham_id = fields.Int(required=True, allow_none=True)
    gia = fields.Float(required=True, allow_none=True)
    thanhtien = fields.Float(required=True, allow_none=True)


class GetCTDonHangListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetCTDonHangListRequest(**data)


class GetCTDonHangListResponseSchema(PagingResponseSchema):
    results = fields.Nested(CTDonHangResponseSchema, many=True, allow_none=True)


class PostCTDonHangRequestSchema(Schema):
    donhang_id = fields.Int(required=True, allow_none=True)
    sanpham_id = fields.Int(required=True, allow_none=True)
    gia = fields.Float(required=True, allow_none=True)
    thanhtien = fields.Float(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostCTDonHangRequest(**data)


class GetCTDonHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetCTDonHangRequest(**data)


class PutCTDonHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    donhang_id = fields.Int(required=True, allow_none=True)
    sanpham_id = fields.Int(required=True, allow_none=True)
    gia = fields.Float(required=True, allow_none=True)
    thanhtien = fields.Float(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutCTDonHangRequest(**data)


class DeleteCTDonHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteCTDonHangRequest(**data)
