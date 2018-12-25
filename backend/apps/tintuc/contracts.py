from typing import Optional
from backend.apps.base.contracts import (
    PagingRequest,
    PagingResponse,
    DEFAULT_LIMIT,
    DEFAULT_OFFSET
)
from datetime import date


class TinTucResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 danhmuc_id: Optional[int] = None,
                 tieude: Optional[str] = None,
                 hinhanh: Optional[str] = None,
                 mota: Optional[str] = None,
                 noidung: Optional[str] = None,
                 ngaydang: Optional[date] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.danhmuc_id = danhmuc_id
        self.tieude = tieude
        self.hinhanh = hinhanh
        self.mota = mota
        self.noidung = noidung
        self.ngaydang = ngaydang
        self.trangthai = trangthai


class GetTinTucListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetTinTucListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 tintuc_status: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [TinTucResponse(**item) for item in tintuc_status]


class PostTinTucRequest(object):
    def __init__(
            self,
            danhmuc_id: int,
            tieude: str,
            hinhanh: str,
            mota: str,
            noidung: str,
            ngaydang: date,
            trangthai: bool
    ):
        self.danhmuc_id = danhmuc_id
        self.tieude = tieude
        self.hinhanh = hinhanh
        self.mota = mota
        self.noidung = noidung
        self.ngaydang = ngaydang
        self.trangthai = trangthai


class GetTinTucRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutTinTucRequest(object):
    def __init__(
            self,
            id: int,
            danhmuc_id: int,
            tieude: str,
            hinhanh: str,
            mota: str,
            noidung: str,
            ngaydang: date,
            trangthai: bool
    ):
        self.id = id
        self.danhmuc_id = danhmuc_id
        self.tieude = tieude
        self.hinhanh = hinhanh
        self.mota = mota
        self.noidung = noidung
        self.ngaydang = ngaydang
        self.trangthai = trangthai


class DeleteTinTucRequest(object):
    def __init__(self, id: int):
        self.id = id
