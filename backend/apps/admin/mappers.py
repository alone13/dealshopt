from marshmallow import Schema, fields, post_load
from backend.apps.base.mappers import (
    PagingResponseSchema,
    PagingRequestSchema
)
from backend.apps.admin.contracts import (
    # Admin
    GetAdminListRequest,
    PostAdminRequest,
    GetAdminRequest,
    PutAdminRequest,
    DeleteAdminRequest,
    # Role
    GetRoleListRequest,
    PostRoleRequest,
    GetRoleRequest,
    PutRoleRequest,
    DeleteRoleRequest,
    # Module
    GetModuleListRequest,
    PostModuleRequest,
    GetModuleRequest,
    PutModuleRequest,
    DeleteModuleRequest,

    # Role_Permission_Module
    GetPermissionListRequest,
    PostPermissionRequest,
    GetPermissionRequest,
    PutPermissionRequest,
    DeletePermissionRequest,

    # Action
    GetHoatDongListRequest,
    PostHoatDongRequest,
    GetHoatDongRequest,
    PutHoatDongRequest,
    DeleteHoatDongRequest,

    # Module_Action
    GetModule_HoatDongListRequest,
    PostModule_HoatDongRequest,
    GetModule_HoatDongRequest,
    PutModule_HoatDongRequest,
    DeleteModule_HoatDongRequest
)


class AdminResponseSchema(Schema):
    id = fields.Int()
    taikhoan_id = fields.Int(required=True, allow_none=True)


class GetAdminListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetAdminListRequest(**data)


class GetAdminListResponseSchema(PagingResponseSchema):
    results = fields.Nested(AdminResponseSchema, many=True, allow_none=True)


class PostAdminRequestSchema(Schema):
    taikhoan_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostAdminRequest(**data)


class GetAdminRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetAdminRequest(**data)


class PutAdminRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    taikhoan_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutAdminRequest(**data)


class DeleteAdminRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteAdminRequest(**data)


class RoleResponseSchema(Schema):
    id = fields.Int()
    ten = fields.Str(required=True, allow_none=True)


class GetRoleListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetRoleListRequest(**data)


class GetRoleListResponseSchema(PagingResponseSchema):
    results = fields.Nested(RoleResponseSchema, many=True, allow_none=True)


class PostRoleRequestSchema(Schema):
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostRoleRequest(**data)


class GetRoleRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetRoleRequest(**data)


class PutRoleRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutRoleRequest(**data)


class DeleteRoleRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteRoleRequest(**data)


class ModuleResponseSchema(Schema):
    id = fields.Int()
    ten = fields.Str(required=True, allow_none=True)


class GetModuleListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetModuleListRequest(**data)


class GetModuleListResponseSchema(PagingResponseSchema):
    results = fields.Nested(ModuleResponseSchema, many=True, allow_none=True)


class PostModuleRequestSchema(Schema):
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostModuleRequest(**data)


class GetModuleRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetModuleRequest(**data)


class PutModuleRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutModuleRequest(**data)


class DeleteModuleRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteModuleRequest(**data)


class PermissionResponseSchema(Schema):
    id = fields.Int()
    module_id = fields.Int(required=True, allow_none=True)
    role_id = fields.Int(required=True, allow_none=True)


class GetPermissionListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetPermissionListRequest(**data)


class GetPermissionListResponseSchema(PagingResponseSchema):
    results = fields.Nested(PermissionResponseSchema, many=True, allow_none=True)


class PostPermissionRequestSchema(Schema):
    module_id = fields.Int(required=True, allow_none=True)
    role_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostPermissionRequest(**data)


class GetPermissionRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetPermissionRequest(**data)


class PutPermissionRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    module_id = fields.Int(required=True, allow_none=True)
    role_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutPermissionRequest(**data)


class DeletePermissionRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeletePermissionRequest(**data)


class HoatDongResponseSchema(Schema):
    id = fields.Int()
    ten = fields.Str(required=True, allow_none=True)


class GetHoatDongListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetHoatDongListRequest(**data)


class GetHoatDongListResponseSchema(PagingResponseSchema):
    results = fields.Nested(HoatDongResponseSchema, many=True, allow_none=True)


class PostHoatDongRequestSchema(Schema):
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostHoatDongRequest(**data)


class GetHoatDongRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetHoatDongRequest(**data)


class PutHoatDongRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    ten = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutHoatDongRequest(**data)


class DeleteHoatDongRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteHoatDongRequest(**data)


class Module_HoatDongResponseSchema(Schema):
    id = fields.Int()
    module_id = fields.Int(required=True, allow_none=True)
    hoatdong_id = fields.Int(required=True, allow_none=True)


class GetModule_HoatDongListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetModule_HoatDongListRequest(**data)


class GetModule_HoatDongListResponseSchema(PagingResponseSchema):
    results = fields.Nested(Module_HoatDongResponseSchema, many=True, allow_none=True)


class PostModule_HoatDongRequestSchema(Schema):
    module_id = fields.Int(required=True, allow_none=True)
    hoatdong_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostModule_HoatDongRequest(**data)


class GetModule_HoatDongRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetModule_HoatDongRequest(**data)


class PutModule_HoatDongRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    module_id = fields.Int(required=True, allow_none=True)
    hoatdong_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutModule_HoatDongRequest(**data)


class DeleteModule_HoatDongRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteModule_HoatDongRequest(**data)
