from typing import Optional
from backend.apps.base.contracts import (
    PagingRequest,
    PagingResponse,
    DEFAULT_LIMIT,
    DEFAULT_OFFSET
)


class DanhMucResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 danhmuccha: Optional[int] = None,
                 tendanhmuc: Optional[str] = None,
                 link: Optional[str] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.danhmuccha = danhmuccha
        self.tendanhmuc = tendanhmuc
        self.link = link
        self.trangthai = trangthai


class GetDanhMucListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetDanhMucListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 danhmuc: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [DanhMucResponse(**item) for item in danhmuc]


class PostDanhMucRequest(object):
    def __init__(self, danhmuccha: int, tendanhmuc: str, link: str, trangthai: bool):
        self.danhmuccha = danhmuccha
        self.tendanhmuc = tendanhmuc
        self.link = link
        self.trangthai = trangthai


class GetDanhMucRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutDanhMucRequest(object):
    def __init__(self, id: int, danhmuccha: int, tendanhmuc: str, link: str, trangthai: bool):
        self.id = id
        self.danhmuccha = danhmuccha
        self.tendanhmuc = tendanhmuc
        self.link = link
        self.trangthai = trangthai


class DeleteDanhMucRequest(object):
    def __init__(self, id: int):
        self.id = id
