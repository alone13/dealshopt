from backend.apps.base.contracts import NoContentResponse
from backend.apps.sanpham.contracts import (
    GetTinhThanhListRequest,
    GetTinhThanhListResponse,
    TinhThanhResponse,
    PostTinhThanhRequest,
    GetTinhThanhRequest,
    PutTinhThanhRequest,
    DeleteTinhThanhRequest,

    GetQuanHuyenListRequest,
    GetQuanHuyenListResponse,
    PostQuanHuyenRequest,
    QuanHuyenResponse,
    GetQuanHuyenRequest,
    PutQuanHuyenRequest,
    DeleteQuanHuyenRequest,

    GetSanPham_BaoMatListRequest,
    GetSanPham_BaoMatListResponse,
    PostSanPham_BaoMatRequest,
    SanPham_BaoMatResponse,
    GetSanPham_BaoMatRequest,
    PutSanPham_BaoMatRequest,
    DeleteSanPham_BaoMatRequest,

    GetSanPham_TrangThaiListRequest,
    GetSanPham_TrangThaiListResponse,
    PostSanPham_TrangThaiRequest,
    SanPham_TrangThaiResponse,
    GetSanPham_TrangThaiRequest,
    PutSanPham_TrangThaiRequest,
    DeleteSanPham_TrangThaiRequest,

    GetAmThucListRequest,
    GetAmThucListResponse,
    PostAmThucRequest,
    AmThucResponse,
    GetAmThucRequest,
    PutAmThucRequest,
    DeleteAmThucRequest,

    GetTheLoai_SanPhamListRequest,
    GetTheLoai_SanPhamListResponse,
    TheLoai_SanPhamResponse,
    PostTheLoai_SanPhamRequest,
    GetTheLoai_SanPhamRequest,
    PutTheLoai_SanPhamRequest,
    DeleteTheLoai_SanPhamRequest,

    GetSanPhamListRequest,
    GetSanPhamListResponse,
    PostSanPhamRequest,
    SanPhamResponse,
    GetSanPhamRequest,
    PutSanPhamRequest,
    DeleteSanPhamRequest,

    GetLuaChon_SanPhamListRequest,
    GetLuaChon_SanPhamListResponse,
    PostLuaChon_SanPhamRequest,
    LuaChon_SanPhamResponse,
    GetLuaChon_SanPhamRequest,
    PutLuaChon_SanPhamRequest,
    DeleteLuaChon_SanPhamRequest,

    GetSanPham_GiaListRequest,
    GetSanPham_GiaListResponse,
    PostSanPham_GiaRequest,
    SanPham_GiaResponse,
    GetSanPham_GiaRequest,
    PutSanPham_GiaRequest,
    DeleteSanPham_GiaRequest,

    GetSanPham_Gia_ChiTietListRequest,
    GetSanPham_Gia_ChiTietListResponse,
    PostSanPham_Gia_ChiTietRequest,
    SanPham_Gia_ChiTietResponse,
    GetSanPham_Gia_ChiTietRequest,
    PutSanPham_Gia_ChiTietRequest,
    DeleteSanPham_Gia_ChiTietRequest
)
from backend.apps.sanpham.repositories import (
    TinhThanhRepository,
    QuanHuyenRepository,
    SanPham_BaoMatRepository,
    SanPham_TrangThaiRepository,
    AmThucRepository,
    TheLoai_SanPhamRepository,
    SanPhamRepository,
    LuaChon_SanPhamRepository,
    SanPham_GiaRepository,
    SanPham_Gia_ChiTietRepository
)
from backend.lib.exceptions import ResourceNotFoundException


class TinhThanhLogic(object):
    @classmethod
    def get_tinhthanh_list(cls, request: GetTinhThanhListRequest, path: str) -> GetTinhThanhListResponse:
        tinhthanh, total_count = TinhThanhRepository.get_tinhthanh_list()
        tinhthanh_dict = [item for item in tinhthanh]
        return GetTinhThanhListResponse(request, path, tinhthanh_dict, total_count)

    @classmethod
    def post_tinhthanh(cls, request: PostTinhThanhRequest) -> TinhThanhResponse:
        tinhthanh = TinhThanhRepository.post_tinhthanh(
            ten=request.ten,
            trangthai=request.trangthai
        )
        return TinhThanhResponse(
            id=tinhthanh.id,
            ten=tinhthanh.ten,
            trangthai=tinhthanh.trangthai
        )

    @classmethod
    def get_tinhthanh(cls, request: GetTinhThanhRequest) -> TinhThanhResponse:
        tinhthanh = TinhThanhRepository.get_detail_tinhthanh(id=request.id)
        if tinhthanh is None:
            raise ResourceNotFoundException
        return TinhThanhResponse(
            id=tinhthanh.id,
            ten=tinhthanh.ten,
            trangthai=tinhthanh.trangthai
        )

    @classmethod
    def put_tinhthanh(cls, request: PutTinhThanhRequest) -> TinhThanhResponse:
        cls.get_tinhthanh(GetTinhThanhRequest(id=request.id))
        tinhthanh = TinhThanhRepository.put_tinhthanh(
            id=request.id,
            ten=request.ten,
            trangthai=request.trangthai
        )
        return TinhThanhResponse(
            id=tinhthanh.id,
            ten=tinhthanh.ten,
            trangthai=tinhthanh.trangthai
        )

    @classmethod
    def delete_tinhthanh(cls, request: DeleteTinhThanhRequest) -> NoContentResponse:
        cls.get_tinhthanh(GetTinhThanhRequest(id=request.id))
        TinhThanhRepository.delete_tinhthanh(id=request.id)
        return NoContentResponse()


class QuanHuyenLogic(object):
    @classmethod
    def get_quanhuyen_list(cls, request: GetQuanHuyenListRequest, path: str) -> GetQuanHuyenListResponse:
        quanhuyen, total_count = QuanHuyenRepository.get_quanhuyen_list()
        quanhuyen_dict = [item for item in quanhuyen]
        return GetQuanHuyenListResponse(request, path, quanhuyen_dict, total_count)

    @classmethod
    def post_quanhuyen(cls, request: PostQuanHuyenRequest) -> QuanHuyenResponse:
        quanhuyen = QuanHuyenRepository.post_quanhuyen(
            tinh_id=request.tinh_id,
            ten=request.ten,
            trangthai=request.trangthai
        )
        return QuanHuyenResponse(
            id=quanhuyen.id,
            tinh_id=quanhuyen.tinh_id,
            ten=quanhuyen.ten,
            trangthai=quanhuyen.trangthai
        )

    @classmethod
    def get_quanhuyen(cls, request: GetQuanHuyenRequest) -> QuanHuyenResponse:
        quanhuyen = QuanHuyenRepository.get_detail_quanhuyen(id=request.id)
        if quanhuyen is None:
            raise ResourceNotFoundException
        return QuanHuyenResponse(
            id=quanhuyen.id,
            tinh_id=quanhuyen.tinh_id,
            ten=quanhuyen.ten,
            trangthai=quanhuyen.trangthai
        )

    @classmethod
    def put_quanhuyen(cls, request: PutQuanHuyenRequest) -> QuanHuyenResponse:
        cls.get_quanhuyen(GetQuanHuyenRequest(id=request.id))
        quanhuyen = QuanHuyenRepository.put_quanhuyen(
            id=request.id,
            tinh_id=request.tinh_id,
            ten=request.ten,
            trangthai=request.trangthai
        )
        return QuanHuyenResponse(
            id=quanhuyen.id,
            tinh_id=quanhuyen.tinh_id,
            ten=quanhuyen.ten,
            trangthai=quanhuyen.trangthai
        )

    @classmethod
    def delete_quanhuyen(cls, request: DeleteQuanHuyenRequest) -> NoContentResponse:
        cls.get_quanhuyen(GetQuanHuyenRequest(id=request.id))
        QuanHuyenRepository.delete_quanhuyen(id=request.id)
        return NoContentResponse()


class SanPham_BaoMatLogic(object):
    @classmethod
    def get_sanpham_baomat_list(cls, request: GetSanPham_BaoMatListRequest, path: str) -> GetSanPham_BaoMatListResponse:
        sanpham_baomat, total_count = SanPham_BaoMatRepository.get_sanpham_baomat_list()
        sanpham_baomat_dict = [item for item in sanpham_baomat]
        return GetSanPham_BaoMatListResponse(request, path, sanpham_baomat_dict, total_count)

    @classmethod
    def post_sanpham_baomat(cls, request: PostSanPham_BaoMatRequest) -> SanPham_BaoMatResponse:
        sanpham_baomat = SanPham_BaoMatRepository.post_sanpham_baomat(ten=request.ten)
        return SanPham_BaoMatResponse(
            id=sanpham_baomat.id,
            ten=sanpham_baomat.ten
        )

    @classmethod
    def get_sanpham_baomat(cls, request: GetSanPham_BaoMatRequest) -> SanPham_BaoMatResponse:
        sanpham_baomat = SanPham_BaoMatRepository.get_detail_sanpham_baomat(id=request.id)
        if sanpham_baomat is None:
            raise ResourceNotFoundException
        return SanPham_BaoMatResponse(
            id=sanpham_baomat.id,
            ten=sanpham_baomat.ten
        )

    @classmethod
    def put_sanpham_baomat(cls, request: PutSanPham_BaoMatRequest) -> SanPham_BaoMatResponse:
        cls.get_sanpham_baomat(GetSanPham_BaoMatRequest(id=request.id))
        sanpham_baomat = SanPham_BaoMatRepository.put_sanpham_baomat(
            id=request.id,
            ten=request.ten
        )
        return SanPham_BaoMatResponse(
            id=sanpham_baomat.id,
            ten=sanpham_baomat.ten
        )

    @classmethod
    def delete_sanpham_baomat(cls, request: DeleteSanPham_BaoMatRequest) -> NoContentResponse:
        cls.get_sanpham_baomat(GetSanPham_BaoMatRequest(id=request.id))
        SanPham_BaoMatRepository.delete_sanpham_baomat(id=request.id)
        return NoContentResponse()


class SanPham_TrangThaiLogic(object):
    @classmethod
    def get_sanpham_trangthai_list(cls, request: GetSanPham_TrangThaiListRequest,
                                   path: str) -> GetSanPham_TrangThaiListResponse:
        sanpham_trangthai, total_count = SanPham_TrangThaiRepository.get_sanpham_trangthai_list()
        sanpham_trangthai_dict = [item for item in sanpham_trangthai]
        return GetSanPham_TrangThaiListResponse(request, path, sanpham_trangthai_dict, total_count)

    @classmethod
    def post_sanpham_trangthai(cls, request: PostSanPham_TrangThaiRequest) -> SanPham_TrangThaiResponse:
        sanpham_trangthai = SanPham_TrangThaiRepository.post_sanpham_trangthai(trangthai=request.trangthai)
        return SanPham_TrangThaiResponse(
            id=sanpham_trangthai.id,
            trangthai=sanpham_trangthai.trangthai
        )

    @classmethod
    def get_sanpham_trangthai(cls, request: GetSanPham_TrangThaiRequest) -> SanPham_TrangThaiResponse:
        sanpham_trangthai = SanPham_TrangThaiRepository.get_detail_sanpham_trangthai(id=request.id)
        if sanpham_trangthai is None:
            raise ResourceNotFoundException
        return SanPham_TrangThaiResponse(
            id=sanpham_trangthai.id,
            trangthai=sanpham_trangthai.trangthai
        )

    @classmethod
    def put_sanpham_trangthai(cls, request: PutSanPham_TrangThaiRequest) -> SanPham_TrangThaiResponse:
        cls.get_sanpham_trangthai(GetSanPham_TrangThaiRequest(id=request.id))
        sanpham_trangthai = SanPham_TrangThaiRepository.put_sanpham_trangthai(
            id=request.id,
            trangthai=request.trangthai
        )
        return SanPham_TrangThaiResponse(
            id=sanpham_trangthai.id,
            trangthai=sanpham_trangthai.trangthai
        )

    @classmethod
    def delete_sanpham_trangthai(cls, request: DeleteSanPham_TrangThaiRequest) -> NoContentResponse:
        cls.get_sanpham_trangthai(GetSanPham_TrangThaiRequest(id=request.id))
        SanPham_TrangThaiRepository.delete_sanpham_trangthai(id=request.id)
        return NoContentResponse()


class AmThucLogic(object):
    @classmethod
    def get_amthuc_list(cls, request: GetAmThucListRequest, path: str) -> GetAmThucListResponse:
        amthuc, total_count = AmThucRepository.get_amthuc_list()
        amthuc_dict = [item for item in amthuc]
        return GetAmThucListResponse(request, path, amthuc_dict, total_count)

    @classmethod
    def post_amthuc(cls, request: PostAmThucRequest) -> AmThucResponse:
        amthuc = AmThucRepository.post_amthuc(ten=request.ten, trangthai=request.trangthai)
        return AmThucResponse(
            id=amthuc.id,
            ten=amthuc.ten,
            trangthai=amthuc.trangthai
        )

    @classmethod
    def get_amthuc(cls, request: GetAmThucRequest) -> AmThucResponse:
        amthuc = AmThucRepository.get_detail_amthuc(id=request.id)
        if amthuc is None:
            raise ResourceNotFoundException
        return AmThucResponse(
            id=amthuc.id,
            ten=amthuc.ten,
            trangthai=amthuc.trangthai
        )

    @classmethod
    def put_amthuc(cls, request: PutAmThucRequest) -> AmThucResponse:
        cls.get_amthuc(GetAmThucRequest(id=request.id))
        amthuc = AmThucRepository.put_amthuc(
            id=request.id,
            ten=request.ten,
            trangthai=request.trangthai
        )
        return AmThucResponse(
            id=amthuc.id,
            ten=amthuc.ten,
            trangthai=amthuc.trangthai
        )

    @classmethod
    def delete_amthuc(cls, request: DeleteAmThucRequest) -> NoContentResponse:
        cls.get_amthuc(GetAmThucRequest(id=request.id))
        AmThucRepository.delete_amthuc(id=request.id)
        return NoContentResponse()


class TheLoai_SanPhamLogic(object):
    @classmethod
    def get_theloai_sanpham_list(cls, request: GetTheLoai_SanPhamListRequest,
                                 path: str) -> GetTheLoai_SanPhamListResponse:
        theloai_sanpham, total_count = TheLoai_SanPhamRepository.get_theloai_sanpham_list()
        theloai_sanpham_dict = [item for item in theloai_sanpham]
        return GetTheLoai_SanPhamListResponse(request, path, theloai_sanpham_dict, total_count)

    @classmethod
    def post_theloai_sanpham(cls, request: PostTheLoai_SanPhamRequest) -> TheLoai_SanPhamResponse:
        theloai_sanpham = TheLoai_SanPhamRepository.post_theloai_sanpham(
            ten=request.ten,
            link=request.link,
            trangthai=request.trangthai
        )
        return TheLoai_SanPhamResponse(
            id=theloai_sanpham.id,
            ten=theloai_sanpham.ten,
            link=theloai_sanpham.link,
            trangthai=theloai_sanpham.trangthai
        )

    @classmethod
    def get_theloai_sanpham(cls, request: GetTheLoai_SanPhamRequest) -> TheLoai_SanPhamResponse:
        theloai_sanpham = TheLoai_SanPhamRepository.get_detail_theloai_sanpham(id=request.id)
        if theloai_sanpham is None:
            raise ResourceNotFoundException
        return TheLoai_SanPhamResponse(
            id=theloai_sanpham.id,
            ten=theloai_sanpham.ten,
            link=theloai_sanpham.link,
            trangthai=theloai_sanpham.trangthai
        )

    @classmethod
    def put_theloai_sanpham(cls, request: PutTheLoai_SanPhamRequest) -> TheLoai_SanPhamResponse:
        cls.get_theloai_sanpham(GetTheLoai_SanPhamRequest(id=request.id))
        theloai_sanpham = TheLoai_SanPhamRepository.put_theloai_sanpham(
            id=request.id,
            ten=request.ten,
            trangthai=request.trangthai
        )
        return TheLoai_SanPhamResponse(
            id=theloai_sanpham.id,
            ten=theloai_sanpham.ten,
            link=theloai_sanpham.link,
            trangthai=theloai_sanpham.trangthai
        )

    @classmethod
    def delete_theloai_sanpham(cls, request: DeleteTheLoai_SanPhamRequest) -> NoContentResponse:
        cls.get_theloai_sanpham(GetTheLoai_SanPhamRequest(id=request.id))
        TheLoai_SanPhamRepository.delete_theloai_sanpham(id=request.id)
        return NoContentResponse()


class SanPhamLogic(object):
    @classmethod
    def get_sanpham_list(cls, request: GetSanPhamListRequest, path: str) -> GetSanPhamListResponse:
        sanpham, total_count = SanPhamRepository.get_sanpham_list()
        sanpham_dict = [item for item in sanpham]
        return GetSanPhamListResponse(request, path, sanpham_dict, total_count)

    @classmethod
    def post_sanpham(cls, request: PostSanPhamRequest) -> SanPhamResponse:
        sanpham = SanPhamRepository.post_sanpham(
            user_cuahang_id=request.user_cuahang_id,
            theloai_id=request.theloai_id,
            danhmuc_id=request.danhmuc_id,
            baomat_id=request.baomat_id,
            trangthai_id=request.trangthai_id,
            amthuc_id=request.amthuc_id,
            tinhthanh_id=request.trangthai_id,
            quanhuyen_id=request.quanhuyen_id,
            tensanpham=request.tensanpham,
            hinhanh=request.hinhanh,
            ngaydang=request.ngaydang,
            soluong=request.soluong
        )
        return SanPhamResponse(
            id=sanpham.id,
            user_cuahang_id=sanpham.user_cuahang_id,
            theloai_id=sanpham.theloai_id,
            danhmuc_id=sanpham.danhmuc_id,
            baomat_id=sanpham.baomat_id,
            trangthai_id=sanpham.trangthai_id,
            amthuc_id=sanpham.amthuc_id,
            tinhthanh_id=sanpham.trangthai_id,
            quanhuyen_id=sanpham.quanhuyen_id,
            tensanpham=sanpham.tensanpham,
            hinhanh=sanpham.hinhanh,
            ngaydang=sanpham.ngaydang,
            soluong=sanpham.soluong
        )

    @classmethod
    def get_sanpham(cls, request: GetSanPhamRequest) -> SanPhamResponse:
        sanpham = SanPhamRepository.get_detail_sanpham(id=request.id)
        if sanpham is None:
            raise ResourceNotFoundException
        return SanPhamResponse(
            id=sanpham.id,
            user_cuahang_id=sanpham.user_cuahang_id,
            theloai_id=sanpham.theloai_id,
            danhmuc_id=sanpham.danhmuc_id,
            baomat_id=sanpham.baomat_id,
            trangthai_id=sanpham.trangthai_id,
            amthuc_id=sanpham.amthuc_id,
            tinhthanh_id=sanpham.trangthai_id,
            quanhuyen_id=sanpham.quanhuyen_id,
            tensanpham=sanpham.tensanpham,
            hinhanh=sanpham.hinhanh,
            ngaydang=sanpham.ngaydang,
            soluong=sanpham.soluong
        )

    @classmethod
    def put_sanpham(cls, request: PutSanPhamRequest) -> SanPhamResponse:
        cls.get_sanpham(GetSanPhamRequest(id=request.id))
        sanpham = SanPhamRepository.put_sanpham(
            id=request.id,
            user_cuahang_id=request.user_cuahang_id,
            theloai_id=request.theloai_id,
            danhmuc_id=request.danhmuc_id,
            baomat_id=request.baomat_id,
            trangthai_id=request.trangthai_id,
            amthuc_id=request.amthuc_id,
            tinhthanh_id=request.trangthai_id,
            quanhuyen_id=request.quanhuyen_id,
            tensanpham=request.tensanpham,
            hinhanh=request.hinhanh,
            ngaydang=request.ngaydang,
            soluong=request.soluong
        )
        return SanPhamResponse(
            id=sanpham.id,
            user_cuahang_id=sanpham.user_cuahang_id,
            theloai_id=sanpham.theloai_id,
            danhmuc_id=sanpham.danhmuc_id,
            baomat_id=sanpham.baomat_id,
            trangthai_id=sanpham.trangthai_id,
            amthuc_id=sanpham.amthuc_id,
            tinhthanh_id=sanpham.trangthai_id,
            quanhuyen_id=sanpham.quanhuyen_id,
            tensanpham=sanpham.tensanpham,
            hinhanh=sanpham.hinhanh,
            ngaydang=sanpham.ngaydang,
            soluong=sanpham.soluong
        )

    @classmethod
    def delete_sanpham(cls, request: DeleteSanPhamRequest) -> NoContentResponse:
        cls.get_sanpham(GetSanPhamRequest(id=request.id))
        SanPhamRepository.delete_sanpham(id=request.id)
        return NoContentResponse()


class LuaChon_SanPhamLogic(object):
    @classmethod
    def get_luachon_sanpham_list(cls, request: GetLuaChon_SanPhamListRequest,
                                 path: str) -> GetLuaChon_SanPhamListResponse:
        luachon_sanpham, total_count = LuaChon_SanPhamRepository.get_luachon_sanpham_list()
        luachon_sanpham_dict = [item for item in luachon_sanpham]
        return GetSanPhamListResponse(request, path, luachon_sanpham_dict, total_count)

    @classmethod
    def post_luachon_sanpham(cls, request: PostLuaChon_SanPhamRequest) -> LuaChon_SanPhamResponse:
        luachon_sanpham = LuaChon_SanPhamRepository.post_luachon_sanpham(
            sanpham_id=request.sanpham_id,
            ten=request.ten
        )
        return LuaChon_SanPhamResponse(
            id=luachon_sanpham.id,
            sanpham_id=luachon_sanpham.sanpham_id,
            ten=luachon_sanpham.ten
        )

    @classmethod
    def get_luachon_sanpham(cls, request: GetLuaChon_SanPhamRequest) -> LuaChon_SanPhamResponse:
        luachon_sanpham = LuaChon_SanPhamRepository.get_detail_luachon_sanpham(id=request.id)
        if luachon_sanpham is None:
            raise ResourceNotFoundException
        return LuaChon_SanPhamResponse(
            id=luachon_sanpham.id,
            sanpham_id=luachon_sanpham.sanpham_id,
            ten=luachon_sanpham.ten
        )

    @classmethod
    def put_luachon_sanpham(cls, request: PutLuaChon_SanPhamRequest) -> LuaChon_SanPhamResponse:
        cls.get_luachon_sanpham(GetLuaChon_SanPhamRequest(id=request.id))
        luachon_sanpham = LuaChon_SanPhamRepository.put_luachon_sanpham(
            id=request.id,
            sanpham_id=request.sanpham_id,
            ten=request.ten
        )
        return LuaChon_SanPhamResponse(
            id=luachon_sanpham.id,
            sanpham_id=luachon_sanpham.sanpham_id,
            ten=luachon_sanpham.ten
        )

    @classmethod
    def delete_luachon_sanpham(cls, request: DeleteLuaChon_SanPhamRequest) -> NoContentResponse:
        cls.get_luachon_sanpham(GetLuaChon_SanPhamRequest(id=request.id))
        LuaChon_SanPhamRepository.delete_luachon_sanpham(id=request.id)
        return NoContentResponse()


class SanPham_GiaLogic(object):
    @classmethod
    def get_sanpham_gia_list(cls, request: GetSanPham_GiaListRequest, path: str) -> GetSanPham_GiaListResponse:
        sanpham_gia, total_count = SanPham_GiaRepository.get_sanpham_gia_list()
        sanpham_gia_dict = [item for item in sanpham_gia]
        return GetSanPham_GiaListResponse(request, path, sanpham_gia_dict, total_count)

    @classmethod
    def post_sanpham_gia(cls, request: PostSanPham_GiaRequest) -> SanPham_GiaResponse:
        sanpham_gia = SanPham_GiaRepository.post_sanpham_gia(
            sanpham_id=request.sanpham_id
        )
        return SanPham_GiaResponse(
            id=sanpham_gia.id,
            sanpham_id=sanpham_gia.sanpham_id
        )

    @classmethod
    def get_sanpham_gia(cls, request: GetSanPham_GiaRequest) -> SanPham_GiaResponse:
        sanpham_gia = SanPham_GiaRepository.get_detail_sanpham_gia(id=request.id)
        if sanpham_gia is None:
            raise ResourceNotFoundException
        return SanPham_GiaResponse(
            id=sanpham_gia.id,
            sanpham_id=sanpham_gia.sanpham_id
        )

    @classmethod
    def put_sanpham_gia(cls, request: PutSanPham_GiaRequest) -> SanPham_GiaResponse:
        cls.get_sanpham_gia(GetSanPham_GiaRequest(id=request.id))
        sanpham_gia = SanPham_GiaRepository.put_sanpham_gia(
            id=request.id,
            sanpham_id=request.sanpham_id
        )
        return SanPham_GiaResponse(
            id=sanpham_gia.id,
            sanpham_id=sanpham_gia.sanpham_id
        )

    @classmethod
    def delete_sanpham_gia(cls, request: DeleteSanPham_GiaRequest) -> NoContentResponse:
        cls.get_sanpham_gia(GetSanPham_GiaRequest(id=request.id))
        SanPham_GiaRepository.delete_sanpham_gia(id=request.id)
        return NoContentResponse()


class SanPham_Gia_ChiTietLogic(object):
    @classmethod
    def get_sanpham_gia_chitiet_list(cls, request: GetSanPham_Gia_ChiTietListRequest,
                                     path: str) -> GetSanPham_Gia_ChiTietListResponse:
        sanpham_gia_chitiet, total_count = SanPham_Gia_ChiTietRepository.get_sanpham_gia_chitiet_list()
        sanpham_gia_chitiet_dict = [item for item in sanpham_gia_chitiet]
        return GetSanPham_Gia_ChiTietListResponse(request, path, sanpham_gia_chitiet_dict, total_count)

    @classmethod
    def post_sanpham_gia_chitiet(cls, request: PostSanPham_Gia_ChiTietRequest) -> SanPham_Gia_ChiTietResponse:
        sanpham_gia_chitiet = SanPham_Gia_ChiTietRepository.post_sanpham_gia_chitiet(
            sanpham_gia_id=request.sanpham_gia_id,
            gia=request.gia,
            ngaybd=request.ngaybd,
            ngaykt=request.ngaykt,
            is_active=request.is_active
        )
        return SanPham_Gia_ChiTietResponse(
            id=sanpham_gia_chitiet.id,
            sanpham_gia_id=sanpham_gia_chitiet.sanpham_gia_id,
            gia=sanpham_gia_chitiet.gia,
            ngaybd=sanpham_gia_chitiet.ngaybd,
            ngaykt=sanpham_gia_chitiet.ngaykt,
            is_active=sanpham_gia_chitiet.is_active
        )

    @classmethod
    def get_sanpham_gia_chitiet(cls, request: GetSanPham_Gia_ChiTietRequest) -> SanPham_Gia_ChiTietResponse:
        sanpham_gia_chitiet = SanPham_Gia_ChiTietRepository.get_detail_sanpham_gia_chitiet(id=request.id)
        if sanpham_gia_chitiet is None:
            raise ResourceNotFoundException
        return SanPham_Gia_ChiTietResponse(
            id=sanpham_gia_chitiet.id,
            sanpham_gia_id=sanpham_gia_chitiet.sanpham_gia_id,
            gia=sanpham_gia_chitiet.gia,
            ngaybd=sanpham_gia_chitiet.ngaybd,
            ngaykt=sanpham_gia_chitiet.ngaykt,
            is_active=sanpham_gia_chitiet.is_active
        )

    @classmethod
    def put_sanpham_gia_chitiet(cls, request: PutSanPham_Gia_ChiTietRequest) -> SanPham_Gia_ChiTietResponse:
        cls.get_sanpham_gia_chitiet(GetSanPham_Gia_ChiTietRequest(id=request.id))
        sanpham_gia_chitiet = SanPham_Gia_ChiTietRepository.put_sanpham_gia_chitiet(
            id=request.id,
            sanpham_gia_id=request.sanpham_gia_id,
            gia=request.gia,
            ngaybd=request.ngaybd,
            ngaykt=request.ngaykt,
            is_active=request.is_active
        )
        return SanPham_Gia_ChiTietResponse(
            id=sanpham_gia_chitiet.id,
            sanpham_gia_id=sanpham_gia_chitiet.sanpham_gia_id,
            gia=sanpham_gia_chitiet.gia,
            ngaybd=sanpham_gia_chitiet.ngaybd,
            ngaykt=sanpham_gia_chitiet.ngaykt,
            is_active=sanpham_gia_chitiet.is_active
        )

    @classmethod
    def delete_sanpham_gia_chitiet(cls, request: DeleteSanPham_Gia_ChiTietRequest) -> NoContentResponse:
        cls.get_sanpham_gia_chitiet(GetSanPham_Gia_ChiTietRequest(id=request.id))
        SanPham_Gia_ChiTietRepository.delete_sanpham_gia_chitiet(id=request.id)
        return NoContentResponse()
