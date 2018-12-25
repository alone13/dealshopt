from backend.apps.base.mappers import NoContentResponseSchema
from backend.apps.base.views import BaseView
from backend.apps.admin.logics import (
    AdminLogic,
    RoleLogic,
    ModuleLogic,
    PermissionLogic,
    HoatDongLogic,
    Module_HoatDongLogic
)
from backend.apps.admin.mappers import (
    # Admin
    GetAdminListRequestSchema,
    GetAdminListResponseSchema,
    PostAdminRequestSchema,
    AdminResponseSchema,
    GetAdminRequestSchema,
    PutAdminRequestSchema,
    DeleteAdminRequestSchema,

    # Role
    GetRoleListRequestSchema,
    GetRoleListResponseSchema,
    PostRoleRequestSchema,
    RoleResponseSchema,
    GetRoleRequestSchema,
    PutRoleRequestSchema,
    DeleteRoleRequestSchema,

    # Module
    GetModuleListRequestSchema,
    GetModuleListResponseSchema,
    PostModuleRequestSchema,
    ModuleResponseSchema,
    GetModuleRequestSchema,
    PutModuleRequestSchema,
    DeleteModuleRequestSchema,

    # Role_Permission_Module
    GetPermissionListRequestSchema,
    GetPermissionListResponseSchema,
    PostPermissionRequestSchema,
    PermissionResponseSchema,
    GetPermissionRequestSchema,
    PutPermissionRequestSchema,
    DeletePermissionRequestSchema,

    # Action
    GetHoatDongListRequestSchema,
    GetHoatDongListResponseSchema,
    DeleteHoatDongRequestSchema,
    HoatDongResponseSchema,
    PutHoatDongRequestSchema,
    GetHoatDongRequestSchema,
    PostHoatDongRequestSchema,

    # Module_Action
    GetModule_HoatDongListRequestSchema,
    GetModule_HoatDongListResponseSchema,
    PostModule_HoatDongRequestSchema,
    Module_HoatDongResponseSchema,
    GetModule_HoatDongRequestSchema,
    PutModule_HoatDongRequestSchema,
    DeleteModule_HoatDongRequestSchema
)


# Admin
class AdminView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetAdminListRequestSchema(),
            response_schema=GetAdminListResponseSchema(),
            logic_method=AdminLogic.get_admin_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostAdminRequestSchema(),
            response_schema=AdminResponseSchema(),
            logic_method=AdminLogic.post_admin
        )


class AdminDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetAdminRequestSchema(),
            response_schema=AdminResponseSchema(),
            logic_method=AdminLogic.get_admin,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutAdminRequestSchema(),
            response_schema=AdminResponseSchema(),
            logic_method=AdminLogic.put_admin,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteAdminRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=AdminLogic.delete_admin,
            code=id
        )


# Role
class RoleView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetRoleListRequestSchema(),
            response_schema=GetRoleListResponseSchema(),
            logic_method=RoleLogic.get_role_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostRoleRequestSchema(),
            response_schema=RoleResponseSchema(),
            logic_method=RoleLogic.post_role
        )


class RoleDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetRoleRequestSchema(),
            response_schema=RoleResponseSchema(),
            logic_method=RoleLogic.get_role,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutRoleRequestSchema(),
            response_schema=RoleResponseSchema(),
            logic_method=RoleLogic.put_role,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteRoleRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=RoleLogic.delete_role,
            code=id
        )


# Module
class ModuleView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetModuleListRequestSchema(),
            response_schema=GetModuleListResponseSchema(),
            logic_method=ModuleLogic.get_module_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostModuleRequestSchema(),
            response_schema=ModuleResponseSchema(),
            logic_method=ModuleLogic.post_module
        )


class ModuleDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetModuleRequestSchema(),
            response_schema=ModuleResponseSchema(),
            logic_method=ModuleLogic.get_module,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutModuleRequestSchema(),
            response_schema=ModuleResponseSchema(),
            logic_method=ModuleLogic.put_module,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteModuleRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=ModuleLogic.delete_module,
            code=id
        )


# Role_Module
class PermissionView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetPermissionListRequestSchema(),
            response_schema=GetPermissionListResponseSchema(),
            logic_method=PermissionLogic.get_permission_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostPermissionRequestSchema(),
            response_schema=PermissionResponseSchema(),
            logic_method=PermissionLogic.post_permission
        )


class PermissionDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetPermissionRequestSchema(),
            response_schema=PermissionResponseSchema(),
            logic_method=PermissionLogic.get_permission,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutPermissionRequestSchema(),
            response_schema=PermissionResponseSchema(),
            logic_method=PermissionLogic.put_permission,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeletePermissionRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=PermissionLogic.delete_permission,
            code=id
        )


# Action
class HoatDongView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetHoatDongListRequestSchema(),
            response_schema=GetHoatDongListResponseSchema(),
            logic_method=HoatDongLogic.get_hoatdong_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostHoatDongRequestSchema(),
            response_schema=HoatDongResponseSchema(),
            logic_method=HoatDongLogic.post_hoatdong
        )


class HoatDongDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetHoatDongRequestSchema(),
            response_schema=HoatDongResponseSchema(),
            logic_method=HoatDongLogic.get_hoatdong,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutHoatDongRequestSchema(),
            response_schema=HoatDongResponseSchema(),
            logic_method=HoatDongLogic.put_hoatdong,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteHoatDongRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=HoatDongLogic.delete_hoatdong,
            code=id
        )


# Module_Action
class Module_HoatDongView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetModule_HoatDongListRequestSchema(),
            response_schema=GetModule_HoatDongListResponseSchema(),
            logic_method=Module_HoatDongLogic.get_module_hoatdong_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostModule_HoatDongRequestSchema(),
            response_schema=Module_HoatDongResponseSchema(),
            logic_method=Module_HoatDongLogic.post_module_hoatdong
        )


class Module_HoatDongDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetModule_HoatDongRequestSchema(),
            response_schema=Module_HoatDongResponseSchema(),
            logic_method=Module_HoatDongLogic.get_module_hoatdong,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutModule_HoatDongRequestSchema(),
            response_schema=Module_HoatDongResponseSchema(),
            logic_method=Module_HoatDongLogic.put_module_hoatdong,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteModule_HoatDongRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=Module_HoatDongLogic.delete_module_hoatdong,
            code=id
        )
