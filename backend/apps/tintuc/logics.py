from backend.apps.base.contracts import NoContentResponse
from backend.apps.tintuc.contracts import (
    GetTinTucListRequest,
    GetTinTucListResponse,
    TinTucResponse,
    PostTinTucRequest,
    GetTinTucRequest,
    PutTinTucRequest,
    DeleteTinTucRequest
)
from backend.apps.tintuc.repositories import TinTucRepository
from backend.lib.exceptions import ResourceNotFoundException


class TinTucLogic(object):
    @classmethod
    def get_tintuc_list(cls, request: GetTinTucListRequest, path: str) -> GetTinTucListResponse:
        tintuc, total_count = TinTucRepository.get_tintuc_list()
        tintuc_dict = [item for item in tintuc]
        return GetTinTucListResponse(request, path, tintuc_dict, total_count)

    @classmethod
    def post_tintuc(cls, request: PostTinTucRequest) -> TinTucResponse:
        tintuc = TinTucRepository.post_tintuc(
            danhmuc_id=request.danhmuc_id,
            tieude=request.tieude,
            hinhanh=request.hinhanh,
            mota=request.mota,
            noidung=request.noidung,
            ngaydang=request.ngaydang,
            trangthai=request.trangthai
        )
        return TinTucResponse(
            id=tintuc.id,
            danhmuc_id=tintuc.danhmuc_id,
            tieude=tintuc.tieude,
            hinhanh=tintuc.hinhanh,
            mota=tintuc.mota,
            noidung=tintuc.noidung,
            ngaydang=tintuc.ngaydang,
            trangthai=tintuc.trangthai
        )

    @classmethod
    def get_tintuc(cls, request: GetTinTucRequest) -> TinTucResponse:
        tintuc = TinTucRepository.get_detail_tintuc(id=request.id)
        if tintuc is None:
            raise ResourceNotFoundException
        return TinTucResponse(
            id=tintuc.id,
            danhmuc_id=tintuc.danhmuc_id,
            tieude=tintuc.tieude,
            hinhanh=tintuc.hinhanh,
            mota=tintuc.mota,
            noidung=tintuc.noidung,
            ngaydang=tintuc.ngaydang,
            trangthai=tintuc.trangthai
        )

    @classmethod
    def put_tintuc(cls, request: PutTinTucRequest) -> TinTucResponse:
        cls.get_tintuc(GetTinTucRequest(id=request.id))
        tintuc = TinTucRepository.put_tintuc(
            id=request.id,
            danhmuc_id=request.danhmuc_id,
            tieude=request.tieude,
            hinhanh=request.hinhanh,
            mota=request.mota,
            noidung=request.noidung,
            ngaydang=request.ngaydang,
            trangthai=request.trangthai
        )
        return TinTucResponse(
            id=tintuc.id,
            danhmuc_id=tintuc.danhmuc_id,
            tieude=tintuc.tieude,
            hinhanh=tintuc.hinhanh,
            mota=tintuc.mota,
            noidung=tintuc.noidung,
            ngaydang=tintuc.ngaydang,
            trangthai=tintuc.trangthai
        )

    @classmethod
    def delete_tintuc(cls, request: DeleteTinTucRequest) -> NoContentResponse:
        cls.get_tintuc(GetTinTucRequest(id=request.id))
        TinTucRepository.delete_tintuc(id=request.id)
        return NoContentResponse()
