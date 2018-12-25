from typing import Optional
from backend.apps.base.contracts import (
    PagingRequest,
    PagingResponse,
    DEFAULT_LIMIT,
    DEFAULT_OFFSET
)


class User_TrangThaiResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 trangthai: Optional[bool] = None
                 ):
        self.id = id
        self.trangthai = trangthai


class GetUser_TrangThaiListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetUser_TrangThaiListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 user_trangthai: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [User_TrangThaiResponse(**item) for item in user_trangthai]


class PostUser_TrangThaiRequest(object):
    def __init__(self, trangthai: bool):
        self.trangthai = trangthai


class GetUser_TrangThaiRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutUser_TrangThaiRequest(object):
    def __init__(self, id: int, trangthai: bool):
        self.id = id
        self.trangthai = trangthai


class DeleteUser_TrangThaiRequest(object):
    def __init__(self, id: int):
        self.id = id


class UserResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 taikhoan_id: Optional[int] = None,
                 user_trangthai_id: Optional[int] = None
                 ):
        self.id = id
        self.taikhoan_id = taikhoan_id
        self.user_trangthai_id = user_trangthai_id


class GetUserListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetUserListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 user: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [UserResponse(**item) for item in user]


class PostUserRequest(object):
    def __init__(self, taikhoan_id: int, user_trangthai_id: int):
        self.taikhoan_id = taikhoan_id
        self.user_trangthai_id = user_trangthai_id


class GetUserRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutUserRequest(object):
    def __init__(self, id: int, taikhoan_id: int, user_trangthai_id: int):
        self.id = id
        self.taikhoan_id = taikhoan_id
        self.user_trangthai_id = user_trangthai_id


class DeleteUserRequest(object):
    def __init__(self, id: int):
        self.id = id


class User_CuaHangResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 user_id: Optional[int] = None,
                 sanpham_id: Optional[int] = None,
                 tencuahang: Optional[str] = None
                 ):
        self.id = id
        self.user_id = user_id
        self.sanpham_id = sanpham_id
        self.tencuahang = tencuahang


class GetUser_CuaHangListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetUser_CuaHangListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 user_cuahang: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [User_CuaHangResponse(**item) for item in user_cuahang]


class PostUser_CuaHangRequest(object):
    def __init__(self, user_id: int, sanpham_id: int, tencuahang: str):
        self.user_id = user_id
        self.sanpham_id = sanpham_id
        self.tencuahang = tencuahang


class GetUser_CuaHangRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutUser_CuaHangRequest(object):
    def __init__(self, id: int, user_id: int, sanpham_id: int, tencuahang: str):
        self.id = id
        self.user_id = user_id
        self.sanpham_id = sanpham_id
        self.tencuahang = tencuahang


class DeleteUser_CuaHangRequest(object):
    def __init__(self, id: int):
        self.id = id
