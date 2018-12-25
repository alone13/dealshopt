from typing import Optional
from backend.apps.base.contracts import (
    PagingRequest,
    PagingResponse,
    DEFAULT_LIMIT,
    DEFAULT_OFFSET
)


class AdminResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 taikhoan_id: Optional[int] = None
                 ):
        self.id = id
        self.taikhoan_id = taikhoan_id


class GetAdminListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetAdminListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 admin: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [AdminResponse(**item) for item in admin]


class PostAdminRequest(object):
    def __init__(self, taikhoan_id: int):
        self.taikhoan_id = taikhoan_id


class GetAdminRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutAdminRequest(object):
    def __init__(self, id: int, taikhoan_id: int):
        self.id = id
        self.taikhoan_id = taikhoan_id


class DeleteAdminRequest(object):
    def __init__(self, id: int):
        self.id = id


class RoleResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 ten: Optional[str] = None
                 ):
        self.id = id
        self.ten = ten


class GetRoleListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetRoleListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 role: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [RoleResponse(**item) for item in role]


class PostRoleRequest(object):
    def __init__(self, ten: str):
        self.ten = ten


class GetRoleRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutRoleRequest(object):
    def __init__(self, id: int, ten: str):
        self.id = id
        self.ten = ten


class DeleteRoleRequest(object):
    def __init__(self, id: int):
        self.id = id


class ModuleResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 ten: Optional[str] = None
                 ):
        self.id = id
        self.ten = ten


class GetModuleListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetModuleListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 module: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [ModuleResponse(**item) for item in module]


class PostModuleRequest(object):
    def __init__(self, ten: str):
        self.ten = ten


class GetModuleRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutModuleRequest(object):
    def __init__(self, id: int, ten: str):
        self.id = id
        self.ten = ten


class DeleteModuleRequest(object):
    def __init__(self, id: int):
        self.id = id


class PermissionResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 module_id: Optional[int] = None,
                 role_id: Optional[int] = None
                 ):
        self.id = id
        self.module_id = module_id
        self.role_id = role_id


class GetPermissionListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetPermissionListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 permission: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [PermissionResponse(**item) for item in permission]


class PostPermissionRequest(object):
    def __init__(self, module_id: int, role_id: int):
        self.module_id = module_id
        self.role_id = role_id


class GetPermissionRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutPermissionRequest(object):
    def __init__(self, id: int, module_id: int, role_id: int):
        self.id = id
        self.module_id = module_id
        self.role_id = role_id


class DeletePermissionRequest(object):
    def __init__(self, id: int):
        self.id = id


class HoatDongResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 ten: Optional[str] = None
                 ):
        self.id = id
        self.ten = ten


class GetHoatDongListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetHoatDongListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 action: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [HoatDongResponse(**item) for item in action]


class PostHoatDongRequest(object):
    def __init__(self, ten: str):
        self.ten = ten


class GetHoatDongRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutHoatDongRequest(object):
    def __init__(self, id: int, ten: str):
        self.id = id
        self.ten = ten


class DeleteHoatDongRequest(object):
    def __init__(self, id: int):
        self.id = id


class Module_HoatDongResponse(object):
    def __init__(self,
                 id: Optional[int] = None,
                 module_id: Optional[int] = None,
                 hoatdong_id: Optional[int] = None
                 ):
        self.id = id
        self.module_id = module_id
        self.hoatdong_id = hoatdong_id


class GetModule_HoatDongListRequest(PagingRequest):
    def __init__(self,
                 limit: Optional[int] = DEFAULT_LIMIT,
                 offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None,
                 ):
        super().__init__(limit=limit, offset=offset, sort=sort)


class GetModule_HoatDongListResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 module_hoatdong: list,
                 total_count: int
                 ):
        super().__init__(request, path, total_count)
        self.results = [Module_HoatDongResponse(**item) for item in module_hoatdong]


class PostModule_HoatDongRequest(object):
    def __init__(self, module_id: int, hoatdong_id: int):
        self.module_id = module_id
        self.hoatdong_id = hoatdong_id


class GetModule_HoatDongRequest(object):
    def __init__(self, id: int):
        self.id = id


class PutModule_HoatDongRequest(object):
    def __init__(self, id: int, module_id: int, hoatdong_id: int):
        self.id = id
        self.module_id = module_id
        self.hoatdong_id = hoatdong_id


class DeleteModule_HoatDongRequest(object):
    def __init__(self, id: int):
        self.id = id
