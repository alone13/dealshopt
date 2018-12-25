from backend.apps.base.mappers import NoContentResponseSchema
from backend.apps.base.views import BaseView
from backend.apps.sanpham.logics import (
    TinhThanhLogic,
    QuanHuyenLogic,
    SanPham_BaoMatLogic,
    SanPham_TrangThaiLogic,
    AmThucLogic,
    TheLoai_SanPhamLogic,
    SanPhamLogic,
    LuaChon_SanPhamLogic,
    SanPham_GiaLogic,
    SanPham_Gia_ChiTietLogic
)
from backend.apps.sanpham.mappers import (
    GetTinhThanhListRequestSchema,
    GetTinhThanhListResponseSchema,
    PostTinhThanhRequestSchema,
    TinhThanhResponseSchema,
    GetTinhThanhRequestSchema,
    PutTinhThanhRequestSchema,
    DeleteTinhThanhRequestSchema,

    GetQuanHuyenListRequestSchema,
    GetQuanHuyenListResponseSchema,
    PostQuanHuyenRequestSchema,
    QuanHuyenResponseSchema,
    GetQuanHuyenRequestSchema,
    PutQuanHuyenRequestSchema,
    DeleteQuanHuyenRequestSchema,

    GetSanPham_BaoMatListRequestSchema,
    GetSanPham_BaoMatListResponseSchema,
    PostSanPham_BaoMatRequestSchema,
    SanPham_BaoMatResponseSchema,
    GetSanPham_BaoMatRequestSchema,
    PutSanPham_BaoMatRequestSchema,
    DeleteSanPham_BaoMatRequestSchema,

    GetSanPham_TrangThaiListRequestSchema,
    GetSanPham_TrangThaiListResponseSchema,
    PostSanPham_TrangThaiRequestSchema,
    SanPham_TrangThaiResponseSchema,
    GetSanPham_TrangThaiRequestSchema,
    PutSanPham_TrangThaiRequestSchema,
    DeleteSanPham_TrangThaiRequestSchema,

    GetAmThucListRequestSchema,
    GetAmThucListResponseSchema,
    PostAmThucRequestSchema,
    AmThucResponseSchema,
    GetAmThucRequestSchema,
    PutAmThucRequestSchema,
    DeleteAmThucRequestSchema,

    GetTheLoai_SanPhamListRequestSchema,
    GetTheLoai_SanPhamListResponseSchema,
    PostTheLoai_SanPhamRequestSchema,
    TheLoai_SanPhamResponseSchema,
    GetTheLoai_SanPhamRequestSchema,
    PutTheLoai_SanPhamRequestSchema,
    DeleteTheLoai_SanPhamRequestSchema,

    GetSanPhamListRequestSchema,
    GetSanPhamListResponseSchema,
    PostSanPhamRequestSchema,
    SanPhamResponseSchema,
    GetSanPhamRequestSchema,
    PutSanPhamRequestSchema,
    DeleteSanPhamRequestSchema,

    GetLuaChon_SanPhamListRequestSchema,
    GetLuaChon_SanPhamListResponseSchema,
    PostLuaChon_SanPhamRequestSchema,
    LuaChon_SanPhamResponseSchema,
    GetLuaChon_SanPhamRequestSchema,
    PutLuaChon_SanPhamRequestSchema,
    DeleteLuaChon_SanPhamRequestSchema,

    GetSanPham_GiaListRequestSchema,
    GetSanPham_GiaListResponseSchema,
    PostSanPham_GiaRequestSchema,
    SanPham_GiaResponseSchema,
    GetSanPham_GiaRequestSchema,
    PutSanPham_GiaRequestSchema,
    DeleteSanPham_GiaRequestSchema,

    GetSanPham_Gia_ChiTietListRequestSchema,
    GetSanPham_Gia_ChiTietListResponseSchema,
    PostSanPham_Gia_ChiTietRequestSchema,
    SanPham_Gia_ChiTietResponseSchema,
    GetSanPham_Gia_ChiTietRequestSchema,
    PutSanPham_Gia_ChiTietRequestSchema,
    DeleteSanPham_Gia_ChiTietRequestSchema
)


class TinhThanhView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetTinhThanhListRequestSchema(),
            response_schema=GetTinhThanhListResponseSchema(),
            logic_method=TinhThanhLogic.get_tinhthanh_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostTinhThanhRequestSchema(),
            response_schema=TinhThanhResponseSchema(),
            logic_method=TinhThanhLogic.post_tinhthanh
        )


class TinhThanhDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetTinhThanhRequestSchema(),
            response_schema=TinhThanhResponseSchema(),
            logic_method=TinhThanhLogic.get_tinhthanh,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutTinhThanhRequestSchema(),
            response_schema=TinhThanhResponseSchema(),
            logic_method=TinhThanhLogic.put_tinhthanh,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteTinhThanhRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=TinhThanhLogic.delete_tinhthanh,
            code=id
        )


class QuanHuyenView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetQuanHuyenListRequestSchema(),
            response_schema=GetQuanHuyenListResponseSchema(),
            logic_method=QuanHuyenLogic.get_quanhuyen_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostQuanHuyenRequestSchema(),
            response_schema=QuanHuyenResponseSchema(),
            logic_method=QuanHuyenLogic.post_quanhuyen
        )


class QuanHuyenDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetQuanHuyenRequestSchema(),
            response_schema=QuanHuyenResponseSchema(),
            logic_method=QuanHuyenLogic.get_quanhuyen,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutQuanHuyenRequestSchema(),
            response_schema=QuanHuyenResponseSchema(),
            logic_method=QuanHuyenLogic.put_quanhuyen,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteQuanHuyenRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=QuanHuyenLogic.delete_quanhuyen,
            code=id
        )


class SanPham_BaoMatView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetSanPham_BaoMatListRequestSchema(),
            response_schema=GetSanPham_BaoMatListResponseSchema(),
            logic_method=SanPham_BaoMatLogic.get_sanpham_baomat_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostSanPham_BaoMatRequestSchema(),
            response_schema=SanPham_BaoMatResponseSchema(),
            logic_method=SanPham_BaoMatLogic.post_sanpham_baomat
        )


class SanPham_BaoMatDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetSanPham_BaoMatRequestSchema(),
            response_schema=SanPham_BaoMatResponseSchema(),
            logic_method=SanPham_BaoMatLogic.get_sanpham_baomat,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutSanPham_BaoMatRequestSchema(),
            response_schema=SanPham_BaoMatResponseSchema(),
            logic_method=SanPham_BaoMatLogic.put_sanpham_baomat,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteSanPham_BaoMatRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=SanPham_BaoMatLogic.delete_sanpham_baomat,
            code=id
        )


class SanPham_TrangThaiView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetSanPham_TrangThaiListRequestSchema(),
            response_schema=GetSanPham_TrangThaiListResponseSchema(),
            logic_method=SanPham_TrangThaiLogic.get_sanpham_trangthai_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostSanPham_TrangThaiRequestSchema(),
            response_schema=SanPham_TrangThaiResponseSchema(),
            logic_method=SanPham_TrangThaiLogic.post_sanpham_trangthai
        )


class SanPham_TrangThaiDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetSanPham_TrangThaiRequestSchema(),
            response_schema=SanPham_TrangThaiResponseSchema(),
            logic_method=SanPham_TrangThaiLogic.get_sanpham_trangthai,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutSanPham_TrangThaiRequestSchema(),
            response_schema=SanPham_TrangThaiResponseSchema(),
            logic_method=SanPham_TrangThaiLogic.put_sanpham_trangthai,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteSanPham_TrangThaiRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=SanPham_TrangThaiLogic.delete_sanpham_trangthai,
            code=id
        )


class AmThucView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetAmThucListRequestSchema(),
            response_schema=GetAmThucListResponseSchema(),
            logic_method=AmThucLogic.get_amthuc_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostAmThucRequestSchema(),
            response_schema=AmThucResponseSchema(),
            logic_method=AmThucLogic.post_amthuc
        )


class AmThucDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetAmThucRequestSchema(),
            response_schema=AmThucResponseSchema(),
            logic_method=AmThucLogic.get_amthuc,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutAmThucRequestSchema(),
            response_schema=AmThucResponseSchema(),
            logic_method=AmThucLogic.put_amthuc,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteAmThucRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=AmThucLogic.delete_amthuc,
            code=id
        )


class TheLoai_SanPhamView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetTheLoai_SanPhamListRequestSchema(),
            response_schema=GetTheLoai_SanPhamListResponseSchema(),
            logic_method=TheLoai_SanPhamLogic.get_theloai_sanpham_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostTheLoai_SanPhamRequestSchema(),
            response_schema=TheLoai_SanPhamResponseSchema(),
            logic_method=TheLoai_SanPhamLogic.post_theloai_sanpham
        )


class TheLoai_SanPhamDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetTheLoai_SanPhamRequestSchema(),
            response_schema=TheLoai_SanPhamResponseSchema(),
            logic_method=TheLoai_SanPhamLogic.get_theloai_sanpham,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutTheLoai_SanPhamRequestSchema(),
            response_schema=TheLoai_SanPhamResponseSchema(),
            logic_method=TheLoai_SanPhamLogic.put_theloai_sanpham,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteTheLoai_SanPhamRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=TheLoai_SanPhamLogic.delete_theloai_sanpham,
            code=id
        )


class SanPhamView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetSanPhamListRequestSchema(),
            response_schema=GetSanPhamListResponseSchema(),
            logic_method=SanPhamLogic.get_sanpham_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostSanPhamRequestSchema(),
            response_schema=SanPhamResponseSchema(),
            logic_method=SanPhamLogic.post_sanpham
        )


class SanPhamDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetSanPhamRequestSchema(),
            response_schema=SanPhamResponseSchema(),
            logic_method=SanPhamLogic.get_sanpham,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutSanPhamRequestSchema(),
            response_schema=SanPhamResponseSchema(),
            logic_method=SanPhamLogic.put_sanpham,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteSanPhamRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=SanPhamLogic.delete_sanpham,
            code=id
        )


class LuaChon_SanPhamView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetLuaChon_SanPhamListRequestSchema(),
            response_schema=GetLuaChon_SanPhamListResponseSchema(),
            logic_method=LuaChon_SanPhamLogic.get_luachon_sanpham_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostLuaChon_SanPhamRequestSchema(),
            response_schema=LuaChon_SanPhamResponseSchema(),
            logic_method=LuaChon_SanPhamLogic.post_luachon_sanpham
        )


class LuaChon_SanPhamDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetLuaChon_SanPhamRequestSchema(),
            response_schema=LuaChon_SanPhamResponseSchema(),
            logic_method=LuaChon_SanPhamLogic.get_luachon_sanpham,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutLuaChon_SanPhamRequestSchema(),
            response_schema=LuaChon_SanPhamResponseSchema(),
            logic_method=LuaChon_SanPhamLogic.put_luachon_sanpham,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteLuaChon_SanPhamRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=LuaChon_SanPhamLogic.delete_luachon_sanpham,
            code=id
        )


class SanPham_GiaView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetSanPham_GiaListRequestSchema(),
            response_schema=GetSanPham_GiaListResponseSchema(),
            logic_method=SanPham_GiaLogic.get_sanpham_gia_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostSanPham_GiaRequestSchema(),
            response_schema=SanPham_GiaResponseSchema(),
            logic_method=SanPham_GiaLogic.post_sanpham_gia
        )


class SanPham_GiaDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetSanPham_GiaRequestSchema(),
            response_schema=SanPham_GiaResponseSchema(),
            logic_method=SanPham_GiaLogic.get_sanpham_gia,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutSanPham_GiaRequestSchema(),
            response_schema=SanPham_GiaResponseSchema(),
            logic_method=SanPham_GiaLogic.put_sanpham_gia,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteSanPham_GiaRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=SanPham_GiaLogic.delete_sanpham_gia,
            code=id
        )


class SanPham_Gia_ChiTietView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetSanPham_Gia_ChiTietListRequestSchema(),
            response_schema=GetSanPham_Gia_ChiTietListResponseSchema(),
            logic_method=SanPham_Gia_ChiTietLogic.get_sanpham_gia_chitiet_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostSanPham_Gia_ChiTietRequestSchema(),
            response_schema=SanPham_Gia_ChiTietResponseSchema(),
            logic_method=SanPham_Gia_ChiTietLogic.post_sanpham_gia_chitiet
        )


class SanPham_Gia_ChiTietDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetSanPham_Gia_ChiTietRequestSchema(),
            response_schema=SanPham_Gia_ChiTietResponseSchema(),
            logic_method=SanPham_Gia_ChiTietLogic.get_sanpham_gia_chitiet,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutSanPham_Gia_ChiTietRequestSchema(),
            response_schema=SanPham_Gia_ChiTietResponseSchema(),
            logic_method=SanPham_Gia_ChiTietLogic.put_sanpham_gia_chitiet,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteSanPham_Gia_ChiTietRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=SanPham_Gia_ChiTietLogic.delete_sanpham_gia_chitiet,
            code=id
        )
