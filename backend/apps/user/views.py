from backend.apps.base.mappers import NoContentResponseSchema
from backend.apps.base.views import BaseView
from backend.apps.user.logics import UserLogic, User_CuaHangLogic, User_TrangThaiLogic
from backend.apps.user.mappers import (
    GetUserListRequestSchema,
    GetUserListResponseSchema,
    PostUserRequestSchema,
    UserResponseSchema,
    GetUserRequestSchema,
    PutUserRequestSchema,
    DeleteUserRequestSchema,

    GetUser_CuaHangListRequestSchema,
    GetUser_CuaHangListResponseSchema,
    PostUser_CuaHangRequestSchema,
    User_CuaHangResponseSchema,
    GetUser_CuaHangRequestSchema,
    PutUser_CuaHangRequestSchema,
    DeleteUser_CuaHangRequestSchema,

    GetUser_TrangThaiListRequestSchema,
    GetUser_TrangThaiListResponseSchema,
    PostUser_TrangThaiRequestSchema,
    User_TrangThaiResponseSchema,
    GetUser_TrangThaiRequestSchema,
    PutUser_TrangThaiRequestSchema,
    DeleteUser_TrangThaiRequestSchema
)


class User_TrangThaiView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetUser_TrangThaiListRequestSchema(),
            response_schema=GetUser_TrangThaiListResponseSchema(),
            logic_method=User_TrangThaiLogic.get_user_trangthai_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostUser_TrangThaiRequestSchema(),
            response_schema=User_TrangThaiResponseSchema(),
            logic_method=User_TrangThaiLogic.post_user_trangthai
        )


class User_TrangThaiDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetUser_TrangThaiRequestSchema(),
            response_schema=User_TrangThaiResponseSchema(),
            logic_method=User_TrangThaiLogic.get_user_trangthai,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutUser_TrangThaiRequestSchema(),
            response_schema=User_TrangThaiResponseSchema(),
            logic_method=User_TrangThaiLogic.put_user_trangthai,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteUser_TrangThaiRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=User_TrangThaiLogic.delete_user_trangthai,
            code=id
        )


class UserView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetUserListRequestSchema(),
            response_schema=GetUserListResponseSchema(),
            logic_method=UserLogic.get_user_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostUserRequestSchema(),
            response_schema=UserResponseSchema(),
            logic_method=UserLogic.post_user
        )


class UserDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetUserRequestSchema(),
            response_schema=UserResponseSchema(),
            logic_method=UserLogic.get_user,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutUserRequestSchema(),
            response_schema=UserResponseSchema(),
            logic_method=UserLogic.put_user,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteUserRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=UserLogic.delete_user,
            code=id
        )


class User_CuaHangView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetUser_CuaHangListRequestSchema(),
            response_schema=GetUser_CuaHangListResponseSchema(),
            logic_method=User_CuaHangLogic.get_user_cuahang_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostUser_CuaHangRequestSchema(),
            response_schema=User_CuaHangResponseSchema(),
            logic_method=User_CuaHangLogic.post_user_cuahang
        )


class User_CuaHangDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetUser_CuaHangRequestSchema(),
            response_schema=User_CuaHangResponseSchema(),
            logic_method=User_CuaHangLogic.get_user_cuahang,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutUser_CuaHangRequestSchema(),
            response_schema=User_CuaHangResponseSchema(),
            logic_method=User_CuaHangLogic.put_user_cuahang,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteUser_CuaHangRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=User_CuaHangLogic.delete_user_cuahang,
            code=id
        )
