from backend.apps.base.contracts import NoContentResponse
from backend.apps.user.contracts import (
    GetUserListRequest,
    GetUserListResponse,
    UserResponse,
    PostUserRequest,
    GetUserRequest,
    PutUserRequest,
    DeleteUserRequest,

    GetUser_CuaHangListRequest,
    GetUser_CuaHangListResponse,
    PostUser_CuaHangRequest,
    User_CuaHangResponse,
    GetUser_CuaHangRequest,
    PutUser_CuaHangRequest,
    DeleteUser_CuaHangRequest,

    GetUser_TrangThaiListRequest,
    GetUser_TrangThaiListResponse,
    PostUser_TrangThaiRequest,
    User_TrangThaiResponse,
    GetUser_TrangThaiRequest,
    PutUser_TrangThaiRequest,
    DeleteUser_TrangThaiRequest
)
from backend.apps.user.repositories import (
    UserRepository,
    User_CuaHang_SanPhamRepository,
    User_TrangThaiRepository)
from backend.lib.exceptions import ResourceNotFoundException


class User_TrangThaiLogic(object):
    @classmethod
    def get_user_trangthai_list(cls, request: GetUser_TrangThaiListRequest, path: str) -> GetUser_TrangThaiListResponse:
        user_trangthai, total_count = User_TrangThaiRepository.get_user_trangthai_list()
        user_dict = [item for item in user_trangthai]
        return GetUser_TrangThaiListResponse(request, path, user_dict, total_count)

    @classmethod
    def post_user_trangthai(cls, request: PostUser_TrangThaiRequest) -> User_TrangThaiResponse:
        user = User_TrangThaiRepository.post_user_trangthai(
            trangthai=request.trangthai
        )
        return User_TrangThaiResponse(
            id=user.id,
            trangthai=user.trangthai
        )

    @classmethod
    def get_user_trangthai(cls, request: GetUser_TrangThaiRequest) -> User_TrangThaiResponse:
        user = User_TrangThaiRepository.get_detail_user_trangthai(id=request.id)
        if user is None:
            raise ResourceNotFoundException
        return User_TrangThaiResponse(
            id=user.id,
            trangthai=user.trangthai
        )

    @classmethod
    def put_user_trangthai(cls, request: PutUser_TrangThaiRequest) -> User_TrangThaiResponse:
        cls.get_user_trangthai(GetUser_TrangThaiRequest(id=request.id))
        user = User_TrangThaiRepository.put_user_trangthai(
            id=request.id,
            trangthai=request.trangthai
        )
        return User_TrangThaiResponse(
            id=user.id,
            trangthai=user.trangthai
        )

    @classmethod
    def delete_user_trangthai(cls, request: DeleteUser_TrangThaiRequest) -> NoContentResponse:
        cls.get_user_trangthai(GetUser_TrangThaiRequest(id=request.id))
        User_TrangThaiRepository.delete_user_trangthai(id=request.id)
        return NoContentResponse()


class UserLogic(object):
    @classmethod
    def get_user_list(cls, request: GetUserListRequest, path: str) -> GetUserListResponse:
        user, total_count = UserRepository.get_user_list()
        user_dict = [item for item in user]
        return GetUserListResponse(request, path, user_dict, total_count)

    @classmethod
    def post_user(cls, request: PostUserRequest) -> UserResponse:
        user = UserRepository.post_user(taikhoan_id=request.taikhoan_id, user_trangthai_id=request.user_trangthai_id)
        return UserResponse(
            id=user.id,
            taikhoan_id=user.taikhoan_id,
            user_trangthai_id=user.user_trangthai_id
        )

    @classmethod
    def get_user(cls, request: GetUserRequest) -> UserResponse:
        user = UserRepository.get_detail_user(id=request.id)
        if user is None:
            raise ResourceNotFoundException
        return UserResponse(
            id=user.id,
            taikhoan_id=user.taikhoan_id,
            user_trangthai_id=user.user_trangthai_id
        )

    @classmethod
    def put_user(cls, request: PutUserRequest) -> UserResponse:
        cls.get_user(GetUserRequest(id=request.id))
        user = UserRepository.put_user(
            id=request.id,
            taikhoan_id=request.taikhoan_id,
            user_trangthai_id=request.user_trangthai_id
        )
        return UserResponse(
            id=user.id,
            taikhoan_id=user.taikhoan_id,
            user_trangthai_id=user.user_trangthai_id
        )

    @classmethod
    def delete_user(cls, request: DeleteUserRequest) -> NoContentResponse:
        cls.get_user(GetUserRequest(id=request.id))
        UserRepository.delete_user(id=request.id)
        return NoContentResponse()


class User_CuaHangLogic(object):
    @classmethod
    def get_user_cuahang_list(cls, request: GetUser_CuaHangListRequest, path: str) -> GetUser_CuaHangListResponse:
        user_cuahang, total_count = User_CuaHang_SanPhamRepository.get_user_cuahang_list()
        user_dict = [item for item in user_cuahang]
        return GetUser_CuaHangListResponse(request, path, user_dict, total_count)

    @classmethod
    def post_user_cuahang(cls, request: PostUser_CuaHangRequest) -> User_CuaHangResponse:
        user = User_CuaHang_SanPhamRepository.post_user_cuahang(
            user_id=request.user_id,
            sanpham_id=request.sanpham_id,
            tencuahang=request.tencuahang
        )
        return User_CuaHangResponse(
            id=user.id,
            user_id=user.user_id,
            sanpham_id=user.sanpham_id,
            tencuahang=user.tencuahang
        )

    @classmethod
    def get_user_cuahang(cls, request: GetUser_CuaHangRequest) -> User_CuaHangResponse:
        user = User_CuaHang_SanPhamRepository.get_detail_user_cuahang(id=request.id)
        if user is None:
            raise ResourceNotFoundException
        return User_CuaHangResponse(
            id=user.id,
            user_id=user.user_id,
            sanpham_id=user.sanpham_id,
            tencuahang=user.tencuahang
        )

    @classmethod
    def put_user_cuahang(cls, request: PutUser_CuaHangRequest) -> User_CuaHangResponse:
        cls.get_user_cuahang(GetUser_CuaHangRequest(id=request.id))
        user = User_CuaHang_SanPhamRepository.put_user_cuahang(
            id=request.id,
            user_id=request.user_id,
            sanpham_id=request.sanpham_id,
            tencuahang=request.tencuahang
        )
        return User_CuaHangResponse(
            id=user.id,
            user_id=user.user_id,
            sanpham_id=user.sanpham_id,
            tencuahang=user.tencuahang
        )

    @classmethod
    def delete_user_cuahang(cls, request: DeleteUser_CuaHangRequest) -> NoContentResponse:
        cls.get_user_cuahang(GetUser_CuaHangRequest(id=request.id))
        User_CuaHang_SanPhamRepository.delete_user_cuahang(id=request.id)
        return NoContentResponse()
