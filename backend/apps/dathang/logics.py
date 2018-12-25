from backend.apps.base.contracts import NoContentResponse
from backend.apps.dathang.contracts import (
    GetKhachHangListRequest,
    GetKhachHangListResponse,
    KhachHangResponse,
    PostKhachHangRequest,
    GetKhachHangRequest,
    PutKhachHangRequest,
    DeleteKhachHangRequest,

    GetDonHangListRequest,
    GetDonHangListResponse,
    PostDonHangRequest,
    DonHangResponse,
    GetDonHangRequest,
    PutDonHangRequest,
    DeleteDonHangRequest,

    GetCTDonHangListRequest,
    GetCTDonHangListResponse,
    PostCTDonHangRequest,
    CTDonHangResponse,
    GetCTDonHangRequest,
    PutCTDonHangRequest,
    DeleteCTDonHangRequest
)
from backend.apps.dathang.repositories import KhachHangRepository, DonHangRepository, CTDonHangRepository
from backend.lib.exceptions import ResourceNotFoundException


class KhachHangLogic(object):
    @classmethod
    def get_khachhang_list(cls, request: GetKhachHangListRequest, path: str) -> GetKhachHangListResponse:
        khachhang, total_count = KhachHangRepository.get_khachhang_list()
        khachhang_dict = [item for item in khachhang]
        return GetKhachHangListResponse(request, path, khachhang_dict, total_count)

    @classmethod
    def post_khachhang(cls, request: PostKhachHangRequest) -> KhachHangResponse:
        khachhang = KhachHangRepository.post_khachhang(
            tenkhachhang=request.tenkhachhang,
            diachi=request.diachi,
            email=request.email,
            sdt=request.sdt
        )
        return KhachHangResponse(
            id=khachhang.id,
            tenkhachhang=khachhang.tenkhachhang,
            diachi=khachhang.diachi,
            email=khachhang.email,
            sdt=khachhang.sdt
        )

    @classmethod
    def get_khachhang(cls, request: GetKhachHangRequest) -> KhachHangResponse:
        khachhang = KhachHangRepository.get_detail_khachhang(id=request.id)
        if khachhang is None:
            raise ResourceNotFoundException
        return KhachHangResponse(
            id=khachhang.id,
            tenkhachhang=khachhang.tenkhachhang,
            diachi=khachhang.diachi,
            email=khachhang.email,
            sdt=khachhang.sdt
        )

    @classmethod
    def put_khachhang(cls, request: PutKhachHangRequest) -> KhachHangResponse:
        cls.get_khachhang(GetKhachHangRequest(id=request.id))
        khachhang = KhachHangRepository.put_khachhang(
            id=request.id,
            tenkhachhang=request.tenkhachhang,
            diachi=request.diachi,
            email=request.email,
            sdt=request.sdt
        )
        return KhachHangResponse(
            id=khachhang.id,
            tenkhachhang=khachhang.tenkhachhang,
            diachi=khachhang.diachi,
            email=khachhang.email,
            sdt=khachhang.sdt
        )

    @classmethod
    def delete_khachhang(cls, request: DeleteKhachHangRequest) -> NoContentResponse:
        cls.get_khachhang(GetKhachHangRequest(id=request.id))
        KhachHangRepository.delete_khachhang(id=request.id)
        return NoContentResponse()


class DonHangLogic(object):
    @classmethod
    def get_donhang_list(cls, request: GetDonHangListRequest, path: str) -> GetDonHangListResponse:
        donhang, total_count = DonHangRepository.get_donhang_list()
        donhang_dict = [item for item in donhang]
        return GetDonHangListResponse(request, path, donhang_dict, total_count)

    @classmethod
    def post_donhang(cls, request: PostDonHangRequest) -> DonHangResponse:
        donhang = DonHangRepository.post_donhang(
            khachhang_id=request.khachhang_id,
            ngaydat=request.ngaydat,
            trangthai=request.trangthai
        )
        return DonHangResponse(
            id=donhang.id,
            khachhang_id=donhang.khachhang_id,
            ngaydat=donhang.ngaydat,
            trangthai=donhang.trangthai
        )

    @classmethod
    def get_donhang(cls, request: GetDonHangRequest) -> DonHangResponse:
        donhang = DonHangRepository.get_detail_donhang(id=request.id)
        if donhang is None:
            raise ResourceNotFoundException
        return DonHangResponse(
            id=donhang.id,
            khachhang_id=donhang.khachhang_id,
            ngaydat=donhang.ngaydat,
            trangthai=donhang.trangthai
        )

    @classmethod
    def put_donhang(cls, request: PutDonHangRequest) -> DonHangResponse:
        cls.get_donhang(GetDonHangRequest(id=request.id))
        donhang = DonHangRepository.put_donhang(
            id=request.id,
            khachhang_id=request.khachhang_id,
            ngaydat=request.ngaydat,
            trangthai=request.trangthai
        )
        return DonHangResponse(
            id=donhang.id,
            khachhang_id=donhang.khachhang_id,
            ngaydat=donhang.ngaydat,
            trangthai=donhang.trangthai
        )

    @classmethod
    def delete_donhang(cls, request: DeleteDonHangRequest) -> NoContentResponse:
        cls.get_donhang(GetDonHangRequest(id=request.id))
        DonHangRepository.delete_donhang(id=request.id)
        return NoContentResponse()


class CTDonHangLogic(object):
    @classmethod
    def get_ctdonhang_list(cls, request: GetCTDonHangListRequest, path: str) -> GetCTDonHangListResponse:
        ctdonhang, total_count = CTDonHangRepository.get_ctdonhang_list()
        ctdonhang_dict = [item for item in ctdonhang]
        return GetCTDonHangListResponse(request, path, ctdonhang_dict, total_count)

    @classmethod
    def post_ctdonhang(cls, request: PostCTDonHangRequest) -> CTDonHangResponse:
        ctdonhang = CTDonHangRepository.post_ctdonhang(
            donhang_id=request.donhang_id,
            sanpham_id=request.sanpham_id,
            gia=request.gia,
            thanhtien=request.thanhtien
        )
        return CTDonHangResponse(
            id=ctdonhang.id,
            donhang_id=ctdonhang.donhang_id,
            sanpham_id=ctdonhang.sanpham_id,
            gia=ctdonhang.gia,
            thanhtien=ctdonhang.thanhtien
        )

    @classmethod
    def get_ctdonhang(cls, request: GetCTDonHangRequest) -> CTDonHangResponse:
        ctdonhang = CTDonHangRepository.get_detail_ctdonhang(id=request.id)
        if ctdonhang is None:
            raise ResourceNotFoundException
        return CTDonHangResponse(
            id=ctdonhang.id,
            donhang_id=ctdonhang.donhang_id,
            sanpham_id=ctdonhang.sanpham_id,
            gia=ctdonhang.gia,
            thanhtien=ctdonhang.thanhtien
        )

    @classmethod
    def put_ctdonhang(cls, request: PutCTDonHangRequest) -> CTDonHangResponse:
        cls.get_ctdonhang(GetCTDonHangRequest(id=request.id))
        ctdonhang = CTDonHangRepository.put_ctdonhang(
            id=request.id,
            donhang_id=request.donhang_id,
            sanpham_id=request.sanpham_id,
            gia=request.gia,
            thanhtien=request.thanhtien
        )
        return CTDonHangResponse(
            id=ctdonhang.id,
            donhang_id=ctdonhang.donhang_id,
            sanpham_id=ctdonhang.sanpham_id,
            gia=ctdonhang.gia,
            thanhtien=ctdonhang.thanhtien
        )

    @classmethod
    def delete_ctdonhang(cls, request: DeleteCTDonHangRequest) -> NoContentResponse:
        cls.get_ctdonhang(GetCTDonHangRequest(id=request.id))
        CTDonHangRepository.delete_ctdonhang(id=request.id)
        return NoContentResponse()
