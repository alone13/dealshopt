from typing import Optional
from backend.apps.base.contracts import (
    PagingRequest,
    PagingResponse,
    DEFAULT_LIMIT,
    DEFAULT_OFFSET
)
from datetime import date


class KhachHangResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 tenkhachhang: Optional[str] = None,
                 diachi: Optional[str] = None,
                 email: Optional[str] = None,
                 sdt: Optional[int] = None
                 ):
        self.id = id
        self.tenkhachhang = tenkhachhang
        self.diachi = diachi
        self.email = email
        self.sdt = sdt


class GetKhachHangListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetKhachHangListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 khachhang_status: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [KhachHangResponse(**item) for item in khachhang_status]


class PostKhachHangRequest(object):
    def __init__(
            self,
            tenkhachhang: str,
            diachi: str,
            email: str,
            sdt: int
    ):
        self.tenkhachhang = tenkhachhang
        self.diachi = diachi
        self.email = email
        self.sdt = sdt


class GetKhachHangRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutKhachHangRequest(object):
    def __init__(
            self,
            id: int,
            tenkhachhang: str,
            diachi: str,
            email: str,
            sdt: int
    ):
        self.id = id
        self.tenkhachhang = tenkhachhang
        self.diachi = diachi
        self.email = email
        self.sdt = sdt


class DeleteKhachHangRequest(object):
    def __init__(self, id: int):
        self.id = id


class DonHangResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 khachhang_id: Optional[int] = None,
                 ngaydat: Optional[date] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.khachhang_id = khachhang_id
        self.ngaydat = ngaydat
        self.trangthai = trangthai


class GetDonHangListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetDonHangListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 donhang_status: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [DonHangResponse(**item) for item in donhang_status]


class PostDonHangRequest(object):
    def __init__(
            self,
            khachhang_id: int,
            ngaydat: date,
            trangthai: bool
    ):
        self.khachhang_id = khachhang_id
        self.ngaydat = ngaydat
        self.trangthai = trangthai


class GetDonHangRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutDonHangRequest(object):
    def __init__(
            self,
            id: int,
            khachhang_id: int,
            ngaydat: date,
            trangthai: bool
    ):
        self.id = id
        self.khachhang_id = khachhang_id
        self.ngaydat = ngaydat
        self.trangthai = trangthai


class DeleteDonHangRequest(object):
    def __init__(self, id: int):
        self.id = id


class CTDonHangResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 donhang_id: Optional[int] = None,
                 sanpham_id: Optional[int] = None,
                 gia: Optional[float] = None,
                 thanhtien: Optional[float] = None
                 ):
        self.id = id
        self.donhang_id = donhang_id
        self.sanpham_id = sanpham_id
        self.gia = gia
        self.thanhtien = thanhtien


class GetCTDonHangListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetCTDonHangListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 ctdonhang_status: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [CTDonHangResponse(**item) for item in ctdonhang_status]


class PostCTDonHangRequest(object):
    def __init__(
            self,
            donhang_id: int,
            sanpham_id: int,
            gia: float,
            thanhtien: float
    ):
        self.donhang_id = donhang_id
        self.sanpham_id = sanpham_id
        self.gia = gia
        self.thanhtien = thanhtien


class GetCTDonHangRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutCTDonHangRequest(object):
    def __init__(
            self,
            id: int,
            donhang_id: int,
            sanpham_id: int,
            gia: float,
            thanhtien: float
    ):
        self.id = id
        self.donhang_id = donhang_id
        self.sanpham_id = sanpham_id
        self.gia = gia
        self.thanhtien = thanhtien


class DeleteCTDonHangRequest(object):
    def __init__(self, id: int):
        self.id = id
