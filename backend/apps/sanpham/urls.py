from django.urls import path
from backend.apps.sanpham.views import(
    TinhThanhView,
    TinhThanhDetailView,
    QuanHuyenView,
    QuanHuyenDetailView,
    SanPham_BaoMatView,
    SanPham_BaoMatDetailView,
    SanPham_TrangThaiView,
    SanPham_TrangThaiDetailView,
    AmThucView,
    AmThucDetailView,
    TheLoai_SanPhamView,
    TheLoai_SanPhamDetailView,
    SanPhamView,
    SanPhamDetailView,
    LuaChon_SanPhamView,
    LuaChon_SanPhamDetailView,
    SanPham_GiaView,
    SanPham_GiaDetailView,
    SanPham_Gia_ChiTietView,
    SanPham_Gia_ChiTietDetailView
)

urlpatterns = [
    path('', TinhThanhView.as_view()),
    path('tinhthanh/([0-9]+)/', TinhThanhDetailView.as_view()),
    path('quanhuyen/', QuanHuyenView.as_view()),
    path('quanhuyen/([0-9]+)/', QuanHuyenDetailView.as_view()),
    path('sanpham_baomat/', SanPham_BaoMatView.as_view()),
    path('sanpham_baomat/([0-9]+)/', SanPham_BaoMatDetailView.as_view()),
    path('sanpham_trangthai/', SanPham_TrangThaiView.as_view()),
    path('sanpham_trangthai/([0-9]+)/', SanPham_TrangThaiDetailView.as_view()),
    path('amthuc/', AmThucView.as_view()),
    path('amthuc/([0-9]+)/', AmThucDetailView.as_view()),
    path('theloai_sanpham/', TheLoai_SanPhamView.as_view()),
    path('theloai_sanpham/([0-9]+)/', TheLoai_SanPhamDetailView.as_view()),
    path('', SanPhamView.as_view()),
    path('sanpham/([0-9]+)/', SanPhamDetailView.as_view()),
    path('luachon_sanpham/', LuaChon_SanPhamView.as_view()),
    path('luachon_sanpham/([0-9]+)/', LuaChon_SanPhamDetailView.as_view()),
    path('sanpham_gia/', SanPham_GiaView.as_view()),
    path('sanpham_gia/([0-9]+)/', SanPham_GiaDetailView.as_view()),
    path('sanpham_gia_chitiet/', SanPham_Gia_ChiTietView.as_view()),
    path('sanpham_gia_chitiet/([0-9]+)/', SanPham_Gia_ChiTietDetailView.as_view())
]
