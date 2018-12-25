from typing import Optional

from backend.apps.sanpham.models import (
    TinhThanh,
    QuanHuyen,
    SanPham_BaoMat,
    SanPham_TrangThai,
    AmThuc,
    TheLoai_SanPham,
    SanPham,
    LuaChon_SanPham,
    SanPham_Gia,
    SanPham_Gia_ChiTiet
)
from datetime import date


class TinhThanhRepository(object):
    @classmethod
    def get_tinhthanh_list(cls, limit: Optional[int] = None,
                           offset: Optional[int] = None,
                           sort: Optional[str] = None,
                           ):
        tinhthanh_qs = TinhThanh.objects.values()

        total_count = len(tinhthanh_qs)

        results = tinhthanh_qs
        return results, total_count

    @classmethod
    def post_tinhthanh(cls, ten: str, trangthai: bool):
        tinhthanh = TinhThanh(ten=ten, trangthai=trangthai)
        tinhthanh.save()
        return tinhthanh

    @classmethod
    def get_detail_tinhthanh(cls, id: int):
        try:
            tinhthanh = TinhThanh.objects.get(pk=id)
        except Exception:
            return None
        return tinhthanh

    @classmethod
    def put_tinhthanh(cls, id: int, ten: str, trangthai: bool):
        tinhthanh = TinhThanh.objects.get(pk=id)
        tinhthanh.ten = ten
        tinhthanh.trangthai = trangthai
        tinhthanh.save()
        return tinhthanh

    @classmethod
    def delete_tinhthanh(cls, id: int):
        tinhthanh = TinhThanh.objects.get(pk=id)
        return tinhthanh.delete()


class QuanHuyenRepository(object):
    @classmethod
    def get_quanhuyen_list(cls, limit: Optional[int] = None,
                           offset: Optional[int] = None,
                           sort: Optional[str] = None,
                           ):
        quanhuyen_qs = QuanHuyen.objects.values()

        total_count = len(quanhuyen_qs)

        results = quanhuyen_qs
        return results, total_count

    @classmethod
    def post_quanhuyen(cls, tinh_id: int, ten: str, trangthai: bool):
        quanhuyen = QuanHuyen(tinh_id=tinh_id, ten=ten, trangthai=trangthai)
        quanhuyen.save()
        return quanhuyen

    @classmethod
    def get_detail_quanhuyen(cls, id: int):
        try:
            quanhuyen = QuanHuyen.objects.get(pk=id)
        except Exception:
            return None
        return quanhuyen

    @classmethod
    def put_quanhuyen(cls, id: int, tinh_id: int, ten: str, trangthai: bool):
        quanhuyen = QuanHuyen.objects.get(pk=id)
        quanhuyen.tinh_id = tinh_id
        quanhuyen.ten = ten
        quanhuyen.trangthai = trangthai
        quanhuyen.save()
        return quanhuyen

    @classmethod
    def delete_quanhuyen(cls, id: int):
        quanhuyen = QuanHuyen.objects.get(pk=id)
        return quanhuyen.delete()


class SanPham_BaoMatRepository(object):
    @classmethod
    def get_sanpham_baomat_list(cls, limit: Optional[int] = None,
                                offset: Optional[int] = None,
                                sort: Optional[str] = None,
                                ):
        sanpham_baomat_qs = SanPham_BaoMat.objects.values()

        total_count = len(sanpham_baomat_qs)

        results = sanpham_baomat_qs
        return results, total_count

    @classmethod
    def post_sanpham_baomat(cls, ten: str):
        sanpham_baomat = SanPham_BaoMat(ten=ten)
        sanpham_baomat.save()
        return sanpham_baomat

    @classmethod
    def get_detail_sanpham_baomat(cls, id: int):
        try:
            sanpham_baomat = SanPham_BaoMat.objects.get(pk=id)
        except Exception:
            return None
        return sanpham_baomat

    @classmethod
    def put_sanpham_baomat(cls, id: int, ten: str):
        sanpham_baomat = SanPham_BaoMat.objects.get(pk=id)
        sanpham_baomat.ten = ten
        sanpham_baomat.save()
        return sanpham_baomat

    @classmethod
    def delete_sanpham_baomat(cls, id: int):
        sanpham_baomat = SanPham_BaoMat.objects.get(pk=id)
        return sanpham_baomat.delete()


class SanPham_TrangThaiRepository(object):
    @classmethod
    def get_sanpham_trangthai_list(cls, limit: Optional[int] = None,
                                   offset: Optional[int] = None,
                                   sort: Optional[str] = None,
                                   ):
        sanpham_trangthai_qs = SanPham_TrangThai.objects.values()

        total_count = len(sanpham_trangthai_qs)

        results = sanpham_trangthai_qs
        return results, total_count

    @classmethod
    def post_sanpham_trangthai(cls, trangthai: bool):
        sanpham_trangthai = SanPham_TrangThai(trangthai=trangthai)
        sanpham_trangthai.save()
        return sanpham_trangthai

    @classmethod
    def get_detail_sanpham_trangthai(cls, id: int):
        try:
            sanpham_trangthai = SanPham_TrangThai.objects.get(pk=id)
        except Exception:
            return None
        return sanpham_trangthai

    @classmethod
    def put_sanpham_trangthai(cls, id: int, trangthai: bool):
        sanpham_trangthai = SanPham_TrangThai.objects.get(pk=id)
        sanpham_trangthai.trangthai = trangthai
        sanpham_trangthai.save()
        return sanpham_trangthai

    @classmethod
    def delete_sanpham_trangthai(cls, id: int):
        sanpham_trangthai = SanPham_TrangThai.objects.get(pk=id)
        return sanpham_trangthai.delete()


class AmThucRepository(object):
    @classmethod
    def get_amthuc_list(cls, limit: Optional[int] = None,
                        offset: Optional[int] = None,
                        sort: Optional[str] = None,
                        ):
        amthuc_qs = AmThuc.objects.values()

        total_count = len(amthuc_qs)

        results = amthuc_qs
        return results, total_count

    @classmethod
    def post_amthuc(cls, ten: str, trangthai: bool):
        amthuc = AmThuc(ten=ten, trangthai=trangthai)
        amthuc.save()
        return amthuc

    @classmethod
    def get_detail_amthuc(cls, id: int):
        try:
            amthuc = AmThuc.objects.get(pk=id)
        except Exception:
            return None
        return amthuc

    @classmethod
    def put_amthuc(cls, id: int, ten: str, trangthai: bool):
        amthuc = AmThuc.objects.get(pk=id)
        amthuc.ten = ten
        amthuc.trangthai = trangthai
        amthuc.save()
        return amthuc

    @classmethod
    def delete_amthuc(cls, id: int):
        amthuc = AmThuc.objects.get(pk=id)
        return amthuc.delete()


class TheLoai_SanPhamRepository(object):
    @classmethod
    def get_theloai_sanpham_list(cls, limit: Optional[int] = None,
                                 offset: Optional[int] = None,
                                 sort: Optional[str] = None,
                                 ):
        theloai_sanpham_qs = TheLoai_SanPham.objects.values()

        total_count = len(theloai_sanpham_qs)

        results = theloai_sanpham_qs
        return results, total_count

    @classmethod
    def post_theloai_sanpham(cls, ten: str, link: str, trangthai: bool):
        theloai_sanpham = TheLoai_SanPham(ten=ten, link=link, trangthai=trangthai)
        theloai_sanpham.save()
        return theloai_sanpham

    @classmethod
    def get_detail_theloai_sanpham(cls, id: int):
        try:
            theloai_sanpham = TheLoai_SanPham.objects.get(pk=id)
        except Exception:
            return None
        return theloai_sanpham

    @classmethod
    def put_theloai_sanpham(cls, id: int, ten: str, link: str, trangthai: bool):
        theloai_sanpham = TheLoai_SanPham.objects.get(pk=id)
        theloai_sanpham.ten = ten
        theloai_sanpham.link = link
        theloai_sanpham.trangthai = trangthai
        theloai_sanpham.save()
        return theloai_sanpham

    @classmethod
    def delete_theloai_sanpham(cls, id: int):
        theloai_sanpham = TheLoai_SanPham.objects.get(pk=id)
        return theloai_sanpham.delete()


class SanPhamRepository(object):
    @classmethod
    def get_sanpham_list(cls, limit: Optional[int] = None,
                         offset: Optional[int] = None,
                         sort: Optional[str] = None,
                         ):
        sanpham_qs = SanPham.objects.values()

        total_count = len(sanpham_qs)

        results = sanpham_qs
        return results, total_count

    @classmethod
    def post_sanpham(
            cls,
            user_cuahang_id: int,
            theloai_id: int,
            danhmuc_id: int,
            baomat_id: int,
            trangthai_id: int,
            amthuc_id: int,
            tinhthanh_id: int,
            quanhuyen_id: int,
            tensanpham: str,
            hinhanh: str,
            ngaydang: date,
            soluong: int
    ):
        sanpham = SanPham(
            user_cuahang_id=user_cuahang_id,
            theloai_id=theloai_id,
            danhmuc_id=danhmuc_id,
            baomat_id=baomat_id,
            trangthai_id=trangthai_id,
            amthuc_id=amthuc_id,
            tinhthanh_id=tinhthanh_id,
            quanhuyen_id=quanhuyen_id,
            tensanpham=tensanpham,
            hinhanh=hinhanh,
            ngaydang=ngaydang,
            soluong=soluong
        )
        sanpham.save()
        return sanpham

    @classmethod
    def get_detail_sanpham(cls, id: int):
        try:
            sanpham = SanPham.objects.get(pk=id)
        except Exception:
            return None
        return sanpham

    @classmethod
    def put_sanpham(
            cls,
            id: int,
            user_cuahang_id: int,
            theloai_id: int,
            danhmuc_id: int,
            baomat_id: int,
            trangthai_id: int,
            amthuc_id: int,
            tinhthanh_id: int,
            quanhuyen_id: int,
            tensanpham: str,
            hinhanh: str,
            ngaydang: date,
            soluong: int
    ):
        sanpham = SanPham.objects.get(pk=id)
        sanpham.user_cuahang_id = user_cuahang_id
        sanpham.theloai_id = theloai_id
        sanpham.danhmuc_id = danhmuc_id
        sanpham.baomat_id = baomat_id
        sanpham.trangthai_id = trangthai_id
        sanpham.amthuc_id = amthuc_id
        sanpham.tinhthanh_id = tinhthanh_id
        sanpham.quanhuyen_id = quanhuyen_id
        sanpham.tensanpham = tensanpham
        sanpham.hinhanh = hinhanh
        sanpham.ngaydang = ngaydang
        sanpham.soluong = soluong
        sanpham.save()
        return sanpham

    @classmethod
    def delete_sanpham(cls, id: int):
        sanpham = SanPham.objects.get(pk=id)
        return sanpham.delete()


class LuaChon_SanPhamRepository(object):
    @classmethod
    def get_luachon_sanpham_list(cls, limit: Optional[int] = None,
                                 offset: Optional[int] = None,
                                 sort: Optional[str] = None,
                                 ):
        luachon_sanpham_qs = LuaChon_SanPham.objects.values()

        total_count = len(luachon_sanpham_qs)

        results = luachon_sanpham_qs
        return results, total_count

    @classmethod
    def post_luachon_sanpham(cls, sanpham_id: int, ten: str):
        luachon_sanpham = LuaChon_SanPham(sanpham_id=sanpham_id, ten=ten)
        luachon_sanpham.save()
        return luachon_sanpham

    @classmethod
    def get_detail_luachon_sanpham(cls, id: int):
        try:
            luachon_sanpham = LuaChon_SanPham.objects.get(pk=id)
        except Exception:
            return None
        return luachon_sanpham

    @classmethod
    def put_luachon_sanpham(cls, id: int, sanpham_id: int, ten: str):
        luachon_sanpham = LuaChon_SanPham.objects.get(pk=id)
        luachon_sanpham.sanpham_id = sanpham_id
        luachon_sanpham.ten = ten
        luachon_sanpham.save()
        return luachon_sanpham

    @classmethod
    def delete_luachon_sanpham(cls, id: int):
        luachon_sanpham = LuaChon_SanPham.objects.get(pk=id)
        return luachon_sanpham.delete()


class SanPham_GiaRepository(object):
    @classmethod
    def get_sanpham_gia_list(cls, limit: Optional[int] = None,
                             offset: Optional[int] = None,
                             sort: Optional[str] = None,
                             ):
        sanpham_gia_qs = SanPham_Gia.objects.values()

        total_count = len(sanpham_gia_qs)

        results = sanpham_gia_qs
        return results, total_count

    @classmethod
    def post_sanpham_gia(cls, sanpham_id: int):
        sanpham_gia = SanPham_Gia(sanpham_id=sanpham_id)
        sanpham_gia.save()
        return sanpham_gia

    @classmethod
    def get_detail_sanpham_gia(cls, id: int):
        try:
            sanpham_gia = SanPham_Gia.objects.get(pk=id)
        except Exception:
            return None
        return sanpham_gia

    @classmethod
    def put_sanpham_gia(cls, id: int, sanpham_id: int):
        sanpham_gia = SanPham_Gia.objects.get(pk=id)
        sanpham_gia.sanpham_id = sanpham_id
        sanpham_gia.save()
        return sanpham_gia

    @classmethod
    def delete_sanpham_gia(cls, id: int):
        sanpham_gia = SanPham_Gia.objects.get(pk=id)
        return sanpham_gia.delete()


class SanPham_Gia_ChiTietRepository(object):
    @classmethod
    def get_sanpham_gia_chitiet_list(cls, limit: Optional[int] = None,
                                     offset: Optional[int] = None,
                                     sort: Optional[str] = None,
                                     ):
        sanpham_gia_chitiet_qs = SanPham_Gia_ChiTiet.objects.values()

        total_count = len(sanpham_gia_chitiet_qs)

        results = sanpham_gia_chitiet_qs
        return results, total_count

    @classmethod
    def post_sanpham_gia_chitiet(cls, sanpham_gia_id: int, gia: float, ngaybd: date, ngaykt: date, is_active: bool):
        sanpham_gia_chitiet = SanPham_Gia_ChiTiet(
            sanpham_gia_id=sanpham_gia_id,
            gia=gia,
            ngaybd=ngaybd,
            ngaykt=ngaykt,
            is_active=is_active
        )
        sanpham_gia_chitiet.save()
        return sanpham_gia_chitiet

    @classmethod
    def get_detail_sanpham_gia_chitiet(cls, id: int):
        try:
            sanpham_gia_chitiet = SanPham_Gia_ChiTiet.objects.get(pk=id)
        except Exception:
            return None
        return sanpham_gia_chitiet

    @classmethod
    def put_sanpham_gia_chitiet(
            cls,
            id: int,
            sanpham_gia_id: int,
            gia: float,
            ngaybd: date,
            ngaykt: date,
            is_active: bool
    ):
        sanpham_gia_chitiet = SanPham_Gia_ChiTiet.objects.get(pk=id)
        sanpham_gia_chitiet.sanpham_gia_id = sanpham_gia_id
        sanpham_gia_chitiet.gia = gia
        sanpham_gia_chitiet.ngaybd = ngaybd
        sanpham_gia_chitiet.ngaykt = ngaykt
        sanpham_gia_chitiet.is_active = is_active
        sanpham_gia_chitiet.save()
        return sanpham_gia_chitiet

    @classmethod
    def delete_sanpham_gia_chitiet(cls, id: int):
        sanpham_gia_chitiet = SanPham_Gia_ChiTiet.objects.get(pk=id)
        return sanpham_gia_chitiet.delete()
