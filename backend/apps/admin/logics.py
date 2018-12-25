from backend.apps.base.contracts import NoContentResponse
from backend.apps.admin.repositories import (
    AdminRepository,
    RoleRepository,
    ModuleRepository,
    Role_ModuleRepository,
    HoatDongRepository,
    Module_HoatDongRepository
)
from backend.apps.admin.contracts import (
    # Admin
    AdminResponse,
    GetAdminListRequest,
    GetAdminListResponse,
    PostAdminRequest,
    GetAdminRequest,
    PutAdminRequest,
    DeleteAdminRequest,

    # Role
    RoleResponse,
    GetRoleListRequest,
    GetRoleListResponse,
    PostRoleRequest,
    GetRoleRequest,
    PutRoleRequest,
    DeleteRoleRequest,

    # Module
    ModuleResponse,
    GetModuleListRequest,
    GetModuleListResponse,
    PostModuleRequest,
    GetModuleRequest,
    PutModuleRequest,
    DeleteModuleRequest,

    # Role_Permission_Module
    PermissionResponse,
    GetPermissionListRequest,
    GetPermissionListResponse,
    PostPermissionRequest,
    GetPermissionRequest,
    PutPermissionRequest,
    DeletePermissionRequest,

    # Action
    HoatDongResponse,
    GetHoatDongListRequest,
    GetHoatDongListResponse,
    PostHoatDongRequest,
    GetHoatDongRequest,
    PutHoatDongRequest,
    DeleteHoatDongRequest,

    # Module_Action
    Module_HoatDongResponse,
    GetModule_HoatDongListRequest,
    GetModule_HoatDongListResponse,
    PostModule_HoatDongRequest,
    GetModule_HoatDongRequest,
    PutModule_HoatDongRequest,
    DeleteModule_HoatDongRequest
)
from backend.lib.exceptions import ResourceNotFoundException


# Admin
class AdminLogic(object):
    @classmethod
    def get_admin_list(cls, request: GetAdminListRequest, path: str) -> GetAdminListResponse:
        admin, total_count = AdminRepository.get_admin_list()
        admin_dict = [item for item in admin]
        return GetAdminListResponse(request, path, admin_dict, total_count)

    @classmethod
    def post_admin(cls, request: PostAdminRequest) -> AdminResponse:
        admin = AdminRepository.post_admin(taikhoan_id=request.taikhoan_id)
        return AdminResponse(id=admin.id, taikhoan_id=admin.taikhoan_id)

    @classmethod
    def get_admin(cls, request: GetAdminRequest) -> AdminResponse:
        admin = AdminRepository.get_detail_admin(id=request.id)
        if admin is None:
            raise ResourceNotFoundException
        return AdminResponse(id=admin.id, taikhoan_id=admin.taikhoan_id)

    @classmethod
    def put_admin(cls, request: PutAdminRequest) -> AdminResponse:
        cls.get_admin(GetAdminRequest(id=request.id))
        admin = AdminRepository.put_admin(id=request.id, taikhoan_id=request.taikhoan_id)
        return AdminResponse(id=admin.id, taikhoan_id=admin.taikhoan_id)

    @classmethod
    def delete_admin(cls, request: DeleteAdminRequest) -> NoContentResponse:
        cls.get_admin(GetAdminRequest(id=request.id))
        AdminRepository.delete_admin(id=request.id)
        return NoContentResponse()


class RoleLogic(object):
    @classmethod
    def get_role_list(cls, request: GetRoleListRequest, path: str) -> GetRoleListResponse:
        role, total_count = RoleRepository.get_role_list()
        role_dict = [item for item in role]
        return GetRoleListResponse(request, path, role_dict, total_count)

    @classmethod
    def post_role(cls, request: PostRoleRequest) -> RoleResponse:
        role = RoleRepository.post_role(ten=request.ten)
        return RoleResponse(id=role.id, ten=role.ten)

    @classmethod
    def get_role(cls, request: GetRoleRequest) -> RoleResponse:
        role = RoleRepository.get_detail_role(id=request.id)
        if role is None:
            raise ResourceNotFoundException
        return RoleResponse(id=role.id, ten=role.ten)

    @classmethod
    def put_role(cls, request: PutRoleRequest) -> RoleResponse:
        cls.get_role(GetRoleRequest(id=request.id))
        role = RoleRepository.put_role(id=request.id, ten=request.ten)
        return RoleResponse(id=role.id, ten=role.ten)

    @classmethod
    def delete_role(cls, request: DeleteRoleRequest) -> NoContentResponse:
        cls.get_role(GetRoleRequest(id=request.id))
        RoleRepository.delete_role(id=request.id)
        return NoContentResponse()


class ModuleLogic(object):
    @classmethod
    def get_module_list(cls, request: GetModuleListRequest, path: str) -> GetModuleListResponse:
        module, total_count = ModuleRepository.get_module_list()
        module_dict = [item for item in module]
        return GetModuleListResponse(request, path, module_dict, total_count)

    @classmethod
    def post_module(cls, request: PostModuleRequest) -> ModuleResponse:
        module = ModuleRepository.post_module(ten=request.ten)
        return ModuleResponse(id=module.id, ten=module.ten)

    @classmethod
    def get_module(cls, request: GetModuleRequest) -> ModuleResponse:
        module = ModuleRepository.get_detail_module(id=request.id)
        if module is None:
            raise ResourceNotFoundException
        return ModuleResponse(id=module.id, ten=module.ten)

    @classmethod
    def put_module(cls, request: PutModuleRequest) -> ModuleResponse:
        cls.get_module(GetModuleRequest(id=request.id))
        module = ModuleRepository.put_module(id=request.id, ten=request.ten)
        return ModuleResponse(id=module.id, ten=module.ten)

    @classmethod
    def delete_module(cls, request: DeleteModuleRequest) -> NoContentResponse:
        cls.get_module(GetModuleRequest(id=request.id))
        ModuleRepository.delete_module(id=request.id)
        return NoContentResponse()


class PermissionLogic(object):
    @classmethod
    def get_permission_list(cls, request: GetPermissionListRequest, path: str) -> GetPermissionListResponse:
        permission, total_count = Role_ModuleRepository.get_admin_list()
        permission_dict = [item for item in permission]
        return GetPermissionListResponse(request, path, permission_dict, total_count)

    @classmethod
    def post_permission(cls, request: PostPermissionRequest) -> PermissionResponse:
        permission = Role_ModuleRepository.post_permission(
            module_id=request.module_id,
            role_id=request.role_id
        )
        return PermissionResponse(id=permission.id, module_id=permission.module_id, role_id=permission.role_id)

    @classmethod
    def get_permission(cls, request: GetPermissionRequest) -> PermissionResponse:
        permission = Role_ModuleRepository.get_detail_permission(id=request.id)
        if permission is None:
            raise ResourceNotFoundException
        return PermissionResponse(id=permission.id, module_id=permission.module_id, role_id=permission.role_id)

    @classmethod
    def put_permission(cls, request: PutPermissionRequest) -> PermissionResponse:
        cls.get_permission(GetPermissionRequest(id=request.id))
        permission = Role_ModuleRepository.put_permission(
            id=request.id,
            module_id=request.module_id,
            role_id=request.role_id
        )
        return PermissionResponse(id=permission.id, module_id=permission.module_id, role_id=permission.role_id)

    @classmethod
    def delete_permission(cls, request: DeletePermissionRequest) -> NoContentResponse:
        cls.get_permission(GetPermissionRequest(id=request.id))
        Role_ModuleRepository.delete_permission(id=request.id)
        return NoContentResponse()


class HoatDongLogic(object):
    @classmethod
    def get_hoatdong_list(cls, request: GetHoatDongListRequest, path: str) -> GetHoatDongListResponse:
        action, total_count = HoatDongRepository.get_hoatdong_list()
        action_dict = [item for item in action]
        return GetHoatDongListResponse(request, path, action_dict, total_count)

    @classmethod
    def post_hoatdong(cls, request: PostHoatDongRequest) -> HoatDongResponse:
        action = HoatDongRepository.post_hoatdong(ten=request.ten)
        return HoatDongResponse(id=action.id, ten=action.ten)

    @classmethod
    def get_hoatdong(cls, request: GetHoatDongRequest) -> HoatDongResponse:
        action = HoatDongRepository.get_detail_hoatdong(id=request.id)
        if action is None:
            raise ResourceNotFoundException
        return HoatDongResponse(id=action.id, ten=action.ten)

    @classmethod
    def put_hoatdong(cls, request: PutHoatDongRequest) -> HoatDongResponse:
        cls.get_hoatdong(GetHoatDongRequest(id=request.id))
        action = HoatDongRepository.put_hoatdong(id=request.id, ten=request.ten)
        return HoatDongResponse(id=action.id, ten=action.ten)

    @classmethod
    def delete_hoatdong(cls, request: DeleteHoatDongRequest) -> NoContentResponse:
        cls.get_hoatdong(GetHoatDongRequest(id=request.id))
        HoatDongRepository.delete_hoatdong(id=request.id)
        return NoContentResponse()


class Module_HoatDongLogic(object):
    @classmethod
    def get_module_hoatdong_list(cls, request: GetModule_HoatDongListRequest,
                                 path: str) -> GetModule_HoatDongListResponse:
        module_hoatdong, total_count = Module_HoatDongRepository.get_module_hoatdong_list()
        module_hoatdong_dict = [item for item in module_hoatdong]
        return GetModule_HoatDongListResponse(request, path, module_hoatdong_dict, total_count)

    @classmethod
    def post_module_hoatdong(cls, request: PostModule_HoatDongRequest) -> Module_HoatDongResponse:
        module_hoatdong = Module_HoatDongRepository.post_module_hoatdong(
            module_id=request.module_id,
            hoatdong_id=request.hoatdong_id
        )
        return Module_HoatDongResponse(
            id=module_hoatdong.id,
            module_id=module_hoatdong.module_id,
            hoatdong_id=module_hoatdong.hoatdong_id
        )

    @classmethod
    def get_module_hoatdong(cls, request: GetModule_HoatDongRequest) -> Module_HoatDongResponse:
        module_hoatdong = Module_HoatDongRepository.get_detail_module_hoatdong(id=request.id)
        if module_hoatdong is None:
            raise ResourceNotFoundException
        return Module_HoatDongResponse(
            id=module_hoatdong.id,
            module_id=module_hoatdong.module_id,
            hoatdong_id=module_hoatdong.hoatdong_id
        )

    @classmethod
    def put_module_hoatdong(cls, request: PutModule_HoatDongRequest) -> Module_HoatDongResponse:
        cls.get_module_hoatdong(GetModule_HoatDongRequest(id=request.id))
        module_hoatdong = Module_HoatDongRepository.put_module_hoatdong(
            id=request.id,
            module_id=request.module_id,
            hoatdong_id=request.hoatdong_id
        )
        return Module_HoatDongResponse(
            id=module_hoatdong.id,
            module_id=module_hoatdong.module_id,
            hoatdong_id=module_hoatdong.hoatdong_id
        )

    @classmethod
    def delete_module_hoatdong(cls, request: DeleteModule_HoatDongRequest) -> NoContentResponse:
        cls.get_module_hoatdong(GetModule_HoatDongRequest(id=request.id))
        Module_HoatDongRepository.delete_module_hoatdong(id=request.id)
        return NoContentResponse()
