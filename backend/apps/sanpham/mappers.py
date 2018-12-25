from marshmallow import Schema, fields, post_load

from backend.apps.base.mappers import (
    PagingResponseSchema,
    PagingRequestSchema
)
from backend.apps.sanpham.contracts import (
    GetTinhThanhListRequest,
    PostTinhThanhRequest,
    GetTinhThanhRequest,
    PutTinhThanhRequest,
    DeleteTinhThanhRequest,

    GetQuanHuyenListRequest,
    PostQuanHuyenRequest,
    GetQuanHuyenRequest,
    PutQuanHuyenRequest,
    DeleteQuanHuyenRequest,

    GetSanPham_BaoMatListRequest,
    PostSanPham_BaoMatRequest,
    GetSanPham_BaoMatRequest,
    PutSanPham_BaoMatRequest,
    DeleteSanPham_BaoMatRequest,

    GetSanPham_TrangThaiListRequest,
    PostSanPham_TrangThaiRequest,
    GetSanPham_TrangThaiRequest,
    PutSanPham_TrangThaiRequest,
    DeleteSanPham_TrangThaiRequest,

    GetAmThucListRequest,
    PostAmThucRequest,
    GetAmThucRequest,
    PutAmThucRequest,
    DeleteAmThucRequest,

    GetTheLoai_SanPhamListRequest,
    PostTheLoai_SanPhamRequest,
    GetTheLoai_SanPhamRequest,
    PutTheLoai_SanPhamRequest,
    DeleteTheLoai_SanPhamRequest,

    GetSanPhamListRequest,
    PostSanPhamRequest,
    GetSanPhamRequest,
    PutSanPhamRequest,
    DeleteSanPhamRequest,

    GetLuaChon_SanPhamRequest,
    PutLuaChon_SanPhamRequest,
    DeleteLuaChon_SanPhamRequest,
    PostLuaChon_SanPhamRequest,
    GetLuaChon_SanPhamListRequest,

    GetSanPham_GiaListRequest,
    PostSanPham_GiaRequest,
    GetSanPham_GiaRequest,
    PutSanPham_GiaRequest,
    DeleteSanPham_GiaRequest,

    GetSanPham_Gia_ChiTietListRequest,
    PostSanPham_Gia_ChiTietRequest,
    GetSanPham_Gia_ChiTietRequest,
    PutSanPham_Gia_ChiTietRequest,
    DeleteSanPham_Gia_ChiTietRequest
)


class TinhThanhResponseSchema(Schema):
    id = fields.Int()
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetTinhThanhListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetTinhThanhListRequest(**data)


class GetTinhThanhListResponseSchema(PagingResponseSchema):
    results = fields.Nested(TinhThanhResponseSchema, many=True, allow_none=True)


class PostTinhThanhRequestSchema(Schema):
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostTinhThanhRequest(**data)


class GetTinhThanhRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetTinhThanhRequest(**data)


class PutTinhThanhRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutTinhThanhRequest(**data)


class DeleteTinhThanhRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteTinhThanhRequest(**data)


class QuanHuyenResponseSchema(Schema):
    id = fields.Int()
    tinh_id = fields.Int(required=True, allow_none=True)
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetQuanHuyenListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetQuanHuyenListRequest(**data)


class GetQuanHuyenListResponseSchema(PagingResponseSchema):
    results = fields.Nested(QuanHuyenResponseSchema, many=True, allow_none=True)


class PostQuanHuyenRequestSchema(Schema):
    tinh_id = fields.Int(required=True, allow_none=True)
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostQuanHuyenRequest(**data)


class GetQuanHuyenRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetQuanHuyenRequest(**data)


class PutQuanHuyenRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    tinh_id = fields.Int(required=True, allow_none=True)
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutQuanHuyenRequest(**data)


class DeleteQuanHuyenRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteQuanHuyenRequest(**data)


class SanPham_BaoMatResponseSchema(Schema):
    id = fields.Int()
    ten = fields.Str(required=True, allow_none=True)


class GetSanPham_BaoMatListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPham_BaoMatListRequest(**data)


class GetSanPham_BaoMatListResponseSchema(PagingResponseSchema):
    results = fields.Nested(SanPham_BaoMatResponseSchema, many=True, allow_none=True)


class PostSanPham_BaoMatRequestSchema(Schema):
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostSanPham_BaoMatRequest(**data)


class GetSanPham_BaoMatRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPham_BaoMatRequest(**data)


class PutSanPham_BaoMatRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutSanPham_BaoMatRequest(**data)


class DeleteSanPham_BaoMatRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteSanPham_BaoMatRequest(**data)


class SanPham_TrangThaiResponseSchema(Schema):
    id = fields.Int()
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetSanPham_TrangThaiListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPham_TrangThaiListRequest(**data)


class GetSanPham_TrangThaiListResponseSchema(PagingResponseSchema):
    results = fields.Nested(SanPham_TrangThaiResponseSchema, many=True, allow_none=True)


class PostSanPham_TrangThaiRequestSchema(Schema):
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostSanPham_TrangThaiRequest(**data)


class GetSanPham_TrangThaiRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPham_TrangThaiRequest(**data)


class PutSanPham_TrangThaiRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutSanPham_TrangThaiRequest(**data)


class DeleteSanPham_TrangThaiRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteSanPham_TrangThaiRequest(**data)


class AmThucResponseSchema(Schema):
    id = fields.Int()
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetAmThucListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetAmThucListRequest(**data)


class GetAmThucListResponseSchema(PagingResponseSchema):
    results = fields.Nested(AmThucResponseSchema, many=True, allow_none=True)


class PostAmThucRequestSchema(Schema):
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostAmThucRequest(**data)


class GetAmThucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetAmThucRequest(**data)


class PutAmThucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    ten = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutAmThucRequest(**data)


class DeleteAmThucRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteAmThucRequest(**data)


class TheLoai_SanPhamResponseSchema(Schema):
    id = fields.Int()
    ten = fields.Str(required=True, allow_none=True)
    link = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetTheLoai_SanPhamListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetTheLoai_SanPhamListRequest(**data)


class GetTheLoai_SanPhamListResponseSchema(PagingResponseSchema):
    results = fields.Nested(TheLoai_SanPhamResponseSchema, many=True, allow_none=True)


class PostTheLoai_SanPhamRequestSchema(Schema):
    ten = fields.Str(required=True, allow_none=True)
    link = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostTheLoai_SanPhamRequest(**data)


class GetTheLoai_SanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetTheLoai_SanPhamRequest(**data)


class PutTheLoai_SanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    ten = fields.Str(required=True, allow_none=True)
    link = fields.Str(required=True, allow_none=True)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutTheLoai_SanPhamRequest(**data)


class DeleteTheLoai_SanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteTheLoai_SanPhamRequest(**data)


class SanPhamResponseSchema(Schema):
    id = fields.Int()
    user_cuahang_id = fields.Int(required=True, allow_none=True)
    theloai_id = fields.Int(required=True, allow_none=True)
    danhmuc_id = fields.Int(required=True, allow_none=True)
    baomat_id = fields.Int(required=True, allow_none=True)
    trangthai_id = fields.Int(required=True, allow_none=True)
    amthuc_id = fields.Int(required=True, allow_none=True)
    tinhthanh_id = fields.Int(required=True, allow_none=True)
    quanhuyen = fields.Int(required=True, allow_none=True)
    tensanpham = fields.Str(required=True, allow_none=True)
    hinhanh = fields.Str(required=True, allow_none=True)
    ngaydang = fields.Date(required=True, allow_none=True)
    soluong = fields.Int(required=True, allow_none=True)


class GetSanPhamListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPhamListRequest(**data)


class GetSanPhamListResponseSchema(PagingResponseSchema):
    results = fields.Nested(SanPhamResponseSchema, many=True, allow_none=True)


class PostSanPhamRequestSchema(Schema):
    user_cuahang_id = fields.Int(required=True, allow_none=True)
    theloai_id = fields.Int(required=True, allow_none=True)
    danhmuc_id = fields.Int(required=True, allow_none=True)
    baomat_id = fields.Int(required=True, allow_none=True)
    trangthai_id = fields.Int(required=True, allow_none=True)
    amthuc_id = fields.Int(required=True, allow_none=True)
    tinhthanh_id = fields.Int(required=True, allow_none=True)
    quanhuyen = fields.Int(required=True, allow_none=True)
    tensanpham = fields.Str(required=True, allow_none=True)
    hinhanh = fields.Str(required=True, allow_none=True)
    ngaydang = fields.Date(required=True, allow_none=True)
    soluong = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostSanPhamRequest(**data)


class GetSanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPhamRequest(**data)


class PutSanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    user_cuahang_id = fields.Int(required=True, allow_none=True)
    theloai_id = fields.Int(required=True, allow_none=True)
    danhmuc_id = fields.Int(required=True, allow_none=True)
    baomat_id = fields.Int(required=True, allow_none=True)
    trangthai_id = fields.Int(required=True, allow_none=True)
    amthuc_id = fields.Int(required=True, allow_none=True)
    tinhthanh_id = fields.Int(required=True, allow_none=True)
    quanhuyen = fields.Int(required=True, allow_none=True)
    tensanpham = fields.Str(required=True, allow_none=True)
    hinhanh = fields.Str(required=True, allow_none=True)
    ngaydang = fields.Date(required=True, allow_none=True)
    soluong = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutSanPhamRequest(**data)


class DeleteSanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteSanPhamRequest(**data)


class LuaChon_SanPhamResponseSchema(Schema):
    id = fields.Int()
    sanpham_id = fields.Int(required=True, allow_none=True)
    ten = fields.Str(required=True, allow_none=True)


class GetLuaChon_SanPhamListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetLuaChon_SanPhamListRequest(**data)


class GetLuaChon_SanPhamListResponseSchema(PagingResponseSchema):
    results = fields.Nested(LuaChon_SanPhamResponseSchema, many=True, allow_none=True)


class PostLuaChon_SanPhamRequestSchema(Schema):
    sanpham_id = fields.Int(required=True, allow_none=True)
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostLuaChon_SanPhamRequest(**data)


class GetLuaChon_SanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetLuaChon_SanPhamRequest(**data)


class PutLuaChon_SanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    sanpham_id = fields.Int(required=True, allow_none=True)
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutLuaChon_SanPhamRequest(**data)


class DeleteLuaChon_SanPhamRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteLuaChon_SanPhamRequest(**data)


class SanPham_GiaResponseSchema(Schema):
    id = fields.Int()
    sanpham_id = fields.Int(required=True, allow_none=True)


class GetSanPham_GiaListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPham_GiaListRequest(**data)


class GetSanPham_GiaListResponseSchema(PagingResponseSchema):
    results = fields.Nested(SanPham_GiaResponseSchema, many=True, allow_none=True)


class PostSanPham_GiaRequestSchema(Schema):
    sanpham_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostSanPham_GiaRequest(**data)


class GetSanPham_GiaRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPham_GiaRequest(**data)


class PutSanPham_GiaRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    sanpham_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutSanPham_GiaRequest(**data)


class DeleteSanPham_GiaRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteSanPham_GiaRequest(**data)


class SanPham_Gia_ChiTietResponseSchema(Schema):
    id = fields.Int()
    sanpham_gia_id = fields.Int(required=True, allow_none=True)
    gia = fields.Float(required=True, allow_none=True)
    ngaybd = fields.Date(required=True, allow_none=True)
    ngaykt = fields.Date(required=True, allow_none=True)
    is_active = fields.Boolean(required=True, allow_none=True)


class GetSanPham_Gia_ChiTietListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPham_Gia_ChiTietListRequest(**data)


class GetSanPham_Gia_ChiTietListResponseSchema(PagingResponseSchema):
    results = fields.Nested(SanPham_Gia_ChiTietResponseSchema, many=True, allow_none=True)


class PostSanPham_Gia_ChiTietRequestSchema(Schema):
    sanpham_gia_id = fields.Int(required=True, allow_none=True)
    gia = fields.Float(required=True, allow_none=True)
    ngaybd = fields.Date(required=True, allow_none=True)
    ngaykt = fields.Date(required=True, allow_none=True)
    is_active = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostSanPham_Gia_ChiTietRequest(**data)


class GetSanPham_Gia_ChiTietRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetSanPham_Gia_ChiTietRequest(**data)


class PutSanPham_Gia_ChiTietRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    sanpham_gia_id = fields.Int(required=True, allow_none=True)
    gia = fields.Float(required=True, allow_none=True)
    ngaybd = fields.Date(required=True, allow_none=True)
    ngaykt = fields.Date(required=True, allow_none=True)
    is_active = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutSanPham_Gia_ChiTietRequest(**data)


class DeleteSanPham_Gia_ChiTietRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteSanPham_Gia_ChiTietRequest(**data)
