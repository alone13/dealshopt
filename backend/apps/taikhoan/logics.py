from backend.apps.base.contracts import NoContentResponse
from backend.apps.taikhoan.contracts import (
    GetTaiKhoanListRequest,
    GetTaiKhoanListResponse,
    TaiKhoanResponse,
    PostTaiKhoanRequest,
    GetTaiKhoanRequest,
    PutTaiKhoanRequest,
    DeleteTaiKhoanRequest
)
from backend.apps.taikhoan.repositories import TaiKhoanRepository
from backend.lib.exceptions import ResourceNotFoundException


class TaiKhoanLogic(object):
    @classmethod
    def get_taikhoan_list(cls, request: GetTaiKhoanListRequest, path: str) -> GetTaiKhoanListResponse:
        taikhoan, total_count = TaiKhoanRepository.get_taikhoan_list()
        taikhoan_dict = [item for item in taikhoan]
        return GetTaiKhoanListResponse(request, path, taikhoan_dict, total_count)

    @classmethod
    def post_taikhoan(cls, request: PostTaiKhoanRequest) -> TaiKhoanResponse:
        taikhoan = TaiKhoanRepository.post_taikhoan(
            tendangnhap=request.tendangnhap,
            matkhau=request.matkhau,
            role_id=request.role_id
        )
        return TaiKhoanResponse(
            id=taikhoan.id,
            tendangnhap=taikhoan.tendangnhap,
            matkhau=taikhoan.matkhau,
            role_id=taikhoan.role_id
        )

    @classmethod
    def get_taikhoan(cls, request: GetTaiKhoanRequest) -> TaiKhoanResponse:
        taikhoan = TaiKhoanRepository.get_detail_taikhoan(id=request.id)
        if taikhoan is None:
            raise ResourceNotFoundException
        return TaiKhoanResponse(
            id=taikhoan.id,
            tendangnhap=taikhoan.tendangnhap,
            matkhau=taikhoan.matkhau,
            role_id=taikhoan.role_id
        )

    @classmethod
    def put_taikhoan(cls, request: PutTaiKhoanRequest) -> TaiKhoanResponse:
        cls.get_taikhoan(GetTaiKhoanRequest(id=request.id))
        taikhoan = TaiKhoanRepository.put_taikhoan(
            id=request.id,
            tendangnhap=request.tendangnhap,
            matkhau=request.matkhau,
            role_id=request.role_id
        )
        return TaiKhoanResponse(
            id=taikhoan.id,
            tendangnhap=taikhoan.tendangnhap,
            matkhau=taikhoan.matkhau,
            role_id=taikhoan.role_id
        )

    @classmethod
    def delete_taikhoan(cls, request: DeleteTaiKhoanRequest) -> NoContentResponse:
        cls.get_taikhoan(GetTaiKhoanRequest(id=request.id))
        TaiKhoanRepository.delete_taikhoan(id=request.id)
        return NoContentResponse()
