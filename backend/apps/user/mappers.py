from marshmallow import Schema, fields, post_load

from backend.apps.base.mappers import (
    PagingResponseSchema,
    PagingRequestSchema
)
from backend.apps.user.contracts import (
    GetUserListRequest,
    PostUserRequest,
    GetUserRequest,
    PutUserRequest,
    DeleteUserRequest,

    GetUser_CuaHangListRequest,
    PostUser_CuaHangRequest,
    GetUser_CuaHangRequest,
    PutUser_CuaHangRequest,
    DeleteUser_CuaHangRequest,

    GetUser_TrangThaiListRequest,
    PostUser_TrangThaiRequest,
    GetUser_TrangThaiRequest,
    PutUser_TrangThaiRequest,
    DeleteUser_TrangThaiRequest
)


class User_TrangThaiResponseSchema(Schema):
    id = fields.Int()
    trangthai = fields.Boolean(required=True, allow_none=True)


class GetUser_TrangThaiListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetUser_TrangThaiListRequest(**data)


class GetUser_TrangThaiListResponseSchema(PagingResponseSchema):
    results = fields.Nested(User_TrangThaiResponseSchema, many=True, allow_none=True)


class PostUser_TrangThaiRequestSchema(Schema):
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostUser_TrangThaiRequest(**data)


class GetUser_TrangThaiRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetUser_TrangThaiRequest(**data)


class PutUser_TrangThaiRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    trangthai = fields.Boolean(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutUser_TrangThaiRequest(**data)


class DeleteUser_TrangThaiRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteUser_TrangThaiRequest(**data)


class UserResponseSchema(Schema):
    id = fields.Int()
    taikhoan_id = fields.Int(required=True, allow_none=True)
    user_trangthai_id = fields.Int(required=True, allow_none=True)


class GetUserListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetUserListRequest(**data)


class GetUserListResponseSchema(PagingResponseSchema):
    results = fields.Nested(UserResponseSchema, many=True, allow_none=True)


class PostUserRequestSchema(Schema):
    taikhoan_id = fields.Int(required=True, allow_none=True)
    user_trangthai_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostUserRequest(**data)


class GetUserRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetUserRequest(**data)


class PutUserRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    taikhoan_id = fields.Int(required=True, allow_none=True)
    user_trangthai_id = fields.Int(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutUserRequest(**data)


class DeleteUserRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteUserRequest(**data)


class User_CuaHangResponseSchema(Schema):
    id = fields.Int()
    user_id = fields.Int(required=True, allow_none=True)
    sanpham_id = fields.Int(required=True, allow_none=True)
    tencuahang = fields.Str(required=True, allow_none=True)


class GetUser_CuaHangListRequestSchema(PagingRequestSchema):
    @post_load
    def convert_interface_from_request(self, data):
        return GetUser_CuaHangListRequest(**data)


class GetUser_CuaHangListResponseSchema(PagingResponseSchema):
    results = fields.Nested(User_CuaHangResponseSchema, many=True, allow_none=True)


class PostUser_CuaHangRequestSchema(Schema):
    user_id = fields.Int(required=True, allow_none=True)
    sanpham_id = fields.Int(required=True, allow_none=True)
    tencuahang = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PostUser_CuaHangRequest(**data)


class GetUser_CuaHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return GetUser_CuaHangRequest(**data)


class PutUser_CuaHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    user_id = fields.Int(required=True, allow_none=True)
    sanpham_id = fields.Int(required=True, allow_none=True)
    tencuahang = fields.Str(required=True, allow_none=True)

    @post_load
    def convert_interface_from_request(self, data):
        return PutUser_CuaHangRequest(**data)


class DeleteUser_CuaHangRequestSchema(Schema):
    id = fields.Int(required=True, allow_none=False)

    @post_load
    def convert_interface_from_request(self, data):
        return DeleteUser_CuaHangRequest(**data)
