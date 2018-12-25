from typing import Optional
from backend.apps.base.contracts import (
    PagingRequest,
    PagingResponse,
    DEFAULT_LIMIT,
    DEFAULT_OFFSET
)
from datetime import date


class TinhThanhResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 ten: Optional[str] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.ten = ten
        self.trangthai = trangthai


class GetTinhThanhListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetTinhThanhListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 tinhthanh: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [TinhThanhResponse(**item) for item in tinhthanh]


class PostTinhThanhRequest(object):
    def __init__(self, ten: str, trangthai: bool):
        self.ten = ten
        self.trangthai = trangthai


class GetTinhThanhRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutTinhThanhRequest(object):
    def __init__(self, id: int, ten: str, trangthai: bool):
        self.id = id
        self.ten = ten
        self.trangthai = trangthai


class DeleteTinhThanhRequest(object):
    def __init__(self, id: int):
        self.id = id


class QuanHuyenResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 tinh_id: Optional[int] = None,
                 ten: Optional[str] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.tinh_id = tinh_id
        self.ten = ten
        self.trangthai = trangthai


class GetQuanHuyenListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetQuanHuyenListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 quanhuyen: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [QuanHuyenResponse(**item) for item in quanhuyen]


class PostQuanHuyenRequest(object):
    def __init__(
            self,
            tinh_id: int,
            ten: str,
            trangthai: bool
    ):
        self.tinh_id = tinh_id
        self.ten = ten
        self.trangthai = trangthai


class GetQuanHuyenRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutQuanHuyenRequest(object):
    def __init__(
            self,
            id: int,
            tinh_id: int,
            ten: str,
            trangthai: bool
    ):
        self.id = id
        self.tinh_id = tinh_id
        self.ten = ten
        self.trangthai = trangthai


class DeleteQuanHuyenRequest(object):
    def __init__(self, id: int):
        self.id = id


class SanPham_BaoMatResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 ten: Optional[str] = None
                 ):
        self.id = id
        self.ten = ten


class GetSanPham_BaoMatListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetSanPham_BaoMatListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 sanpham_baomat: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [SanPham_BaoMatResponse(**item) for item in sanpham_baomat]


class PostSanPham_BaoMatRequest(object):
    def __init__(self, ten: str):
        self.ten = ten


class GetSanPham_BaoMatRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutSanPham_BaoMatRequest(object):
    def __init__(self, id: int, ten: str):
        self.id = id
        self.ten = ten


class DeleteSanPham_BaoMatRequest(object):
    def __init__(self, id: int):
        self.id = id


class SanPham_TrangThaiResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.trangthai = trangthai


class GetSanPham_TrangThaiListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetSanPham_TrangThaiListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 sanpham_trangthai: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [SanPham_TrangThaiResponse(**item) for item in sanpham_trangthai]


class PostSanPham_TrangThaiRequest(object):
    def __init__(self, trangthai: bool):
        self.trangthai = trangthai


class GetSanPham_TrangThaiRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutSanPham_TrangThaiRequest(object):
    def __init__(self, id: int, trangthai: bool):
        self.id = id
        self.trangthai = trangthai


class DeleteSanPham_TrangThaiRequest(object):
    def __init__(self, id: int):
        self.id = id


class AmThucResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 ten: Optional[str] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.ten = ten
        self.trangthai = trangthai


class GetAmThucListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetAmThucListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 amthuc: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [AmThucResponse(**item) for item in amthuc]


class PostAmThucRequest(object):
    def __init__(self, ten: str, trangthai: bool):
        self.ten = ten
        self.trangthai = trangthai


class GetAmThucRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutAmThucRequest(object):
    def __init__(self, id: int, ten: str, trangthai: bool):
        self.id = id
        self.ten = ten
        self.trangthai = trangthai


class DeleteAmThucRequest(object):
    def __init__(self, id: int):
        self.id = id


class TheLoai_SanPhamResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 ten: Optional[str] = None,
                 link: Optional[str] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.ten = ten
        self.link = link
        self.trangthai = trangthai


class GetTheLoai_SanPhamListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetTheLoai_SanPhamListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 theloai_sanpham: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [TheLoai_SanPhamResponse(**item) for item in theloai_sanpham]


class PostTheLoai_SanPhamRequest(object):
    def __init__(self, ten: str, link: str, trangthai: bool):
        self.ten = ten
        self.link = link
        self.trangthai = trangthai


class GetTheLoai_SanPhamRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutTheLoai_SanPhamRequest(object):
    def __init__(self, id: int, ten: str, link: str, trangthai: bool):
        self.id = id
        self.ten = ten
        self.link = link
        self.trangthai = trangthai


class DeleteTheLoai_SanPhamRequest(object):
    def __init__(self, id: int):
        self.id = id


class SanPhamResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 user_cuahang_id: Optional[int] = None,
                 theloai_id: Optional[int] = None,
                 danhmuc_id: Optional[int] = None,
                 baomat_id: Optional[int] = None,
                 trangthai_id: Optional[int] = None,
                 amthuc_id: Optional[int] = None,
                 tinhthanh_id: Optional[int] = None,
                 quanhuyen_id: Optional[int] = None,
                 tensanpham: Optional[str] = None,
                 hinhanh: Optional[str] = None,
                 ngaydang: Optional[date] = None,
                 soluong: Optional[int] = None
                 ):
        self.id = id
        self.user_cuahang_id = user_cuahang_id
        self.theloai_id = theloai_id
        self.danhmuc_id = danhmuc_id
        self.baomat_id = baomat_id
        self.trangthai_id = trangthai_id
        self.amthuc_id = amthuc_id
        self.tinhthanh_id = tinhthanh_id
        self.quanhuyen_id = quanhuyen_id
        self.tensanpham = tensanpham
        self.hinhanh = hinhanh
        self.ngaydang = ngaydang
        self.soluong = soluong


class GetSanPhamListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetSanPhamListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 sanpham: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [SanPhamResponse(**item) for item in sanpham]


class PostSanPhamRequest(object):
    def __init__(
            self,
            user_cuahang_id: int,
            theloai_id: int,
            danhmuc_id: int,
            baomat_id: int,
            trangthai_id: int,
            amthuc_id: int,
            tinhthanh_id: int,
            quanhuyen_id: int,
            tensanpham: str,
            hinhanh: str,
            ngaydang: date,
            soluong: int
    ):
        self.user_cuahang_id = user_cuahang_id
        self.theloai_id = theloai_id
        self.danhmuc_id = danhmuc_id
        self.baomat_id = baomat_id
        self.trangthai_id = trangthai_id
        self.amthuc_id = amthuc_id
        self.tinhthanh_id = tinhthanh_id
        self.quanhuyen_id = quanhuyen_id
        self.tensanpham = tensanpham
        self.hinhanh = hinhanh
        self.ngaydang = ngaydang
        self.soluong = soluong


class GetSanPhamRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutSanPhamRequest(object):
    def __init__(
            self,
            id: int,
            user_cuahang_id: int,
            theloai_id: int,
            danhmuc_id: int,
            baomat_id: int,
            trangthai_id: int,
            amthuc_id: int,
            tinhthanh_id: int,
            quanhuyen_id: int,
            tensanpham: str,
            hinhanh: str,
            ngaydang: date,
            soluong: int
    ):
        self.id = id
        self.user_cuahang_id = user_cuahang_id
        self.theloai_id = theloai_id
        self.danhmuc_id = danhmuc_id
        self.baomat_id = baomat_id
        self.trangthai_id = trangthai_id
        self.amthuc_id = amthuc_id
        self.tinhthanh_id = tinhthanh_id
        self.quanhuyen_id = quanhuyen_id
        self.tensanpham = tensanpham
        self.hinhanh = hinhanh
        self.ngaydang = ngaydang
        self.soluong = soluong


class DeleteSanPhamRequest(object):
    def __init__(self, id: int):
        self.id = id


class LuaChon_SanPhamResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 sanpham_id: Optional[int] = None,
                 ten: Optional[str] = None
                 ):
        self.id = id
        self.sanpham_id = sanpham_id
        self.ten = ten


class GetLuaChon_SanPhamListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetLuaChon_SanPhamListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 luachon_sanpham: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [LuaChon_SanPhamResponse(**item) for item in luachon_sanpham]


class PostLuaChon_SanPhamRequest(object):
    def __init__(self, sanpham_id: int, ten: str):
        self.sanpham_id = sanpham_id
        self.ten = ten


class GetLuaChon_SanPhamRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutLuaChon_SanPhamRequest(object):
    def __init__(self, id: int, sanpham_id: int, ten: str):
        self.id = id
        self.sanpham_id = sanpham_id
        self.ten = ten


class DeleteLuaChon_SanPhamRequest(object):
    def __init__(self, id: int):
        self.id = id


class SanPham_GiaResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 sanpham_id: Optional[int] = None
                 ):
        self.id = id
        self.sanpham_id = sanpham_id


class GetSanPham_GiaListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetSanPham_GiaListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 sanpham_gia: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [SanPham_GiaResponse(**item) for item in sanpham_gia]


class PostSanPham_GiaRequest(object):
    def __init__(self, sanpham_id: int):
        self.sanpham_id = sanpham_id


class GetSanPham_GiaRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutSanPham_GiaRequest(object):
    def __init__(self, id: int, sanpham_id: int):
        self.id = id
        self.sanpham_id = sanpham_id


class DeleteSanPham_GiaRequest(object):
    def __init__(self, id: int):
        self.id = id


class SanPham_Gia_ChiTietResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 sanpham_gia_id: Optional[int] = None,
                 gia: Optional[float] = None,
                 ngaybd: Optional[date] = None,
                 ngaykt: Optional[date] = None,
                 is_active: Optional[bool] = None
                 ):
        self.id = id
        self.sanpham_gia_id = sanpham_gia_id
        self.gia = gia
        self.ngaybd = ngaybd
        self.ngaykt = ngaykt
        self.is_active = is_active


class GetSanPham_Gia_ChiTietListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetSanPham_Gia_ChiTietListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 sanpham_gia_chitiet: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [SanPham_Gia_ChiTietResponse(**item) for item in sanpham_gia_chitiet]


class PostSanPham_Gia_ChiTietRequest(object):
    def __init__(self, sanpham_gia_id: int, gia: float, ngaybd: date, ngaykt: date, is_active: bool):
        self.sanpham_gia_id = sanpham_gia_id
        self.gia = gia
        self.ngaybd = ngaybd
        self.ngaykt = ngaykt
        self.is_active = is_active


class GetSanPham_Gia_ChiTietRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutSanPham_Gia_ChiTietRequest(object):
    def __init__(self, id: int, sanpham_gia_id: int, gia: float, ngaybd: date, ngaykt: date, is_active: bool):
        self.id = id
        self.sanpham_gia_id = sanpham_gia_id
        self.gia = gia
        self.ngaybd = ngaybd
        self.ngaykt = ngaykt
        self.is_active = is_active


class DeleteSanPham_Gia_ChiTietRequest(object):
    def __init__(self, id: int):
        self.id = id
