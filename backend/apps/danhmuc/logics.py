from backend.apps.base.contracts import NoContentResponse
from backend.apps.danhmuc.contracts import (
    GetDanhMucListRequest,
    GetDanhMucListResponse,
    DanhMucResponse,
    PostDanhMucRequest,
    GetDanhMucRequest,
    PutDanhMucRequest,
    DeleteDanhMucRequest,
)
from backend.apps.danhmuc.repositories import DanhMucRepository
from backend.lib.exceptions import ResourceNotFoundException


class DanhMucLogic(object):
    @classmethod
    def get_danhmuc_list(cls, request: GetDanhMucListRequest, path: str) -> GetDanhMucListResponse:
        danhmuc, total_count = DanhMucRepository.get_danhmuc_list()
        danhmuc_dict = [item for item in danhmuc]
        return GetDanhMucListResponse(request, path, danhmuc_dict, total_count)

    @classmethod
    def post_danhmuc(cls, request: PostDanhMucRequest) -> DanhMucResponse:
        danhmuc = DanhMucRepository.post_danhmuc(
            danhmuccha=request.danhmuccha,
            tendanhmuc=request.tendanhmuc,
            link=request.link,
            trangthai=request.trangthai
        )
        return DanhMucResponse(
            id=danhmuc.id,
            danhmuccha=danhmuc.danhmuccha,
            tendanhmuc=danhmuc.tendanhmuc,
            link=danhmuc.link,
            trangthai=danhmuc.trangthai
        )

    @classmethod
    def get_danhmuc(cls, request: GetDanhMucRequest) -> DanhMucResponse:
        danhmuc = DanhMucRepository.get_detail_danhmuc(id=request.id)
        if danhmuc is None:
            raise ResourceNotFoundException
        return DanhMucResponse(
            id=danhmuc.id,
            danhmuccha=danhmuc.danhmuccha,
            tendanhmuc=danhmuc.tendanhmuc,
            link=danhmuc.link,
            trangthai=danhmuc.trangthai
        )

    @classmethod
    def put_danhmuc(cls, request: PutDanhMucRequest) -> DanhMucResponse:
        cls.get_danhmuc(GetDanhMucRequest(id=request.id))
        danhmuc = DanhMucRepository.put_danhmuc(
            id=request.id,
            danhmuccha=request.danhmuccha,
            tendanhmuc=request.tendanhmuc,
            link=request.link,
            trangthai=request.trangthai
        )
        return DanhMucResponse(
            id=danhmuc.id,
            danhmuccha=danhmuc.danhmuccha,
            tendanhmuc=danhmuc.tendanhmuc,
            link=danhmuc.link,
            trangthai=danhmuc.trangthai
        )

    @classmethod
    def delete_danhmuc(cls, request: DeleteDanhMucRequest) -> NoContentResponse:
        cls.get_danhmuc(GetDanhMucRequest(id=request.id))
        DanhMucRepository.delete_danhmuc(id=request.id)
        return NoContentResponse()
