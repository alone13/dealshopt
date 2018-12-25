from typing import Optional

from backend.apps.tintuc.models import TinTuc
from datetime import date


class TinTucRepository(object):
    @classmethod
    def get_tintuc_list(cls, limit: Optional[int] = None,
                        offset: Optional[int] = None,
                        sort: Optional[str] = None,
                        ):
        tintuc_qs = TinTuc.objects.values()

        total_count = len(tintuc_qs)

        results = tintuc_qs
        return results, total_count

    @classmethod
    def post_tintuc(
            cls,
            danhmuc_id: int,
            tieude: str,
            hinhanh: str,
            mota: str,
            noidung: str,
            ngaydang: date,
            trangthai: bool
    ):
        tintuc = TinTuc(
            danhmuc_id=danhmuc_id,
            tieude=tieude,
            hinhanh=hinhanh,
            mota=mota,
            noidung=noidung,
            ngaydang=ngaydang,
            trangthai=trangthai
        )
        tintuc.save()
        return tintuc

    @classmethod
    def get_detail_tintuc(cls, id: int):
        try:
            tintuc = TinTuc.objects.get(pk=id)
        except Exception:
            return None
        return tintuc

    @classmethod
    def put_tintuc(
            cls,
            id: int,
            danhmuc_id: int,
            tieude: str,
            hinhanh: str,
            mota: str,
            noidung: str,
            ngaydang: date,
            trangthai: bool
    ):
        tintuc = TinTuc.objects.get(pk=id)
        tintuc.danhmuc_id = danhmuc_id
        tintuc.tieude = tieude
        tintuc.hinhanh = hinhanh
        tintuc.mota = mota
        tintuc.noidung = noidung
        tintuc.ngaydang = ngaydang
        tintuc.trangthai = trangthai
        tintuc.save()
        return tintuc

    @classmethod
    def delete_tintuc(cls, id: int):
        tintuc = TinTuc.objects.get(pk=id)
        return tintuc.delete()
