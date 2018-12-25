from typing import Optional

from backend.apps.dathang.models import KhachHang, DonHang, CTDonHang
from datetime import date


class KhachHangRepository(object):
    @classmethod
    def get_khachhang_list(cls, limit: Optional[int] = None,
                           offset: Optional[int] = None,
                           sort: Optional[str] = None,
                           ):
        khachhang_qs = KhachHang.objects.values()

        total_count = len(khachhang_qs)

        results = khachhang_qs
        return results, total_count

    @classmethod
    def post_khachhang(
            cls,
            tenkhachhang: str,
            diachi: str,
            email: str,
            sdt: int
    ):
        khachhang = KhachHang(
            tenkhachhang=tenkhachhang,
            diachi=diachi,
            email=email,
            sdt=sdt
        )
        khachhang.save()
        return khachhang

    @classmethod
    def get_detail_khachhang(cls, id: int):
        try:
            khachhang = KhachHang.objects.get(pk=id)
        except Exception:
            return None
        return khachhang

    @classmethod
    def put_khachhang(
            cls,
            id: int,
            tenkhachhang: str,
            diachi: str,
            email: str,
            sdt: int
    ):
        khachhang = KhachHang.objects.get(pk=id)
        khachhang.tenkhachhang = tenkhachhang
        khachhang.diachi = diachi
        khachhang.email = email
        khachhang.sdt = sdt
        khachhang.save()
        return khachhang

    @classmethod
    def delete_khachhang(cls, id: int):
        khachhang = KhachHang.objects.get(pk=id)
        return khachhang.delete()


class DonHangRepository(object):
    @classmethod
    def get_donhang_list(cls, limit: Optional[int] = None,
                         offset: Optional[int] = None,
                         sort: Optional[str] = None,
                         ):
        donhang_qs = DonHang.objects.values()

        total_count = len(donhang_qs)

        results = donhang_qs
        return results, total_count

    @classmethod
    def post_donhang(
            cls,
            khachhang_id: int,
            ngaydat: date,
            trangthai: bool
    ):
        donhhang = DonHang(
            khachhang_id=khachhang_id,
            ngaydat=ngaydat,
            trangthai=trangthai
        )
        donhhang.save()
        return donhhang

    @classmethod
    def get_detail_donhang(cls, id: int):
        try:
            donhang = DonHang.objects.get(pk=id)
        except Exception:
            return None
        return donhang

    @classmethod
    def put_donhang(
            cls,
            id: int,
            khachhang_id: int,
            ngaydat: date,
            trangthai: bool
    ):
        donhang = DonHang.objects.get(pk=id)
        donhang.khachhang_id = khachhang_id
        donhang.ngaydat = ngaydat
        donhang.trangthai = trangthai
        donhang.save()
        return donhang

    @classmethod
    def delete_donhang(cls, id: int):
        donhang = DonHang.objects.get(pk=id)
        return donhang.delete()


class CTDonHangRepository(object):
    @classmethod
    def get_ctdonhang_list(cls, limit: Optional[int] = None,
                           offset: Optional[int] = None,
                           sort: Optional[str] = None,
                           ):
        ctdonhang_qs = CTDonHang.objects.values()

        total_count = len(ctdonhang_qs)

        results = ctdonhang_qs
        return results, total_count

    @classmethod
    def post_ctdonhang(
            cls,
            donhang_id: int,
            sanpham_id: int,
            gia: float,
            thanhtien: float
    ):
        ctdonhang = CTDonHang(
            donhang_id=donhang_id,
            sanpham_id=sanpham_id,
            gia=gia,
            thanhtien=thanhtien
        )
        ctdonhang.save()
        return ctdonhang

    @classmethod
    def get_detail_ctdonhang(cls, id: int):
        try:
            ctdonhang = CTDonHang.objects.get(pk=id)
        except Exception:
            return None
        return ctdonhang

    @classmethod
    def put_ctdonhang(
            cls,
            id: int,
            donhang_id: int,
            sanpham_id: int,
            gia: float,
            thanhtien: float
    ):
        ctdonhang = CTDonHang.objects.get(pk=id)
        ctdonhang.donhang_id = donhang_id
        ctdonhang.sanpham_id = sanpham_id
        ctdonhang.gia = gia
        ctdonhang.thanhtien = thanhtien
        ctdonhang.save()
        return ctdonhang

    @classmethod
    def delete_ctdonhang(cls, id: int):
        ctdonhang = CTDonHang.objects.get(pk=id)
        return ctdonhang.delete()
