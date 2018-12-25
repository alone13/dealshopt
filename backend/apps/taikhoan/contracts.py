from typing import Optional
from backend.apps.base.contracts import (
    PagingRequest,
    PagingResponse,
    DEFAULT_LIMIT,
    DEFAULT_OFFSET
)


class TaiKhoanResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 tendangnhap: Optional[str] = None,
                 matkhau: Optional[str] = None,
                 role_id: Optional[int] = None
                 ):
        self.id = id
        self.tendangnhap = tendangnhap
        self.matkhau = matkhau
        self.role_id = role_id


class GetTaiKhoanListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetTaiKhoanListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 taikhoan: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [TaiKhoanResponse(**item) for item in taikhoan]


class PostTaiKhoanRequest(object):
    def __init__(self, tendangnhap: str, matkhau: str, role_id: int):
        self.tendangnhap = tendangnhap
        self.matkhau = matkhau
        self.role_id = role_id


class GetTaiKhoanRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutTaiKhoanRequest(object):
    def __init__(self, id: int, tendangnhap: str, matkhau: str, role_id: int):
        self.id = id
        self.tendangnhap = tendangnhap
        self.matkhau = matkhau
        self.role_id = role_id


class DeleteTaiKhoanRequest(object):
    def __init__(self, id: int):
        self.id = id
