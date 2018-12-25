from typing import Optional

from backend.apps.taikhoan.models import TaiKhoan


class TaiKhoanRepository(object):
    @classmethod
    def get_taikhoan_list(cls, limit: Optional[int] = None,
                          offset: Optional[int] = None,
                          sort: Optional[str] = None,
                          ):
        taikhoan_qs = TaiKhoan.objects.values()

        total_count = len(taikhoan_qs)

        results = taikhoan_qs
        return results, total_count

    @classmethod
    def post_taikhoan(cls, tendangnhap: str, matkhau: str, role_id: int):
        taikhoan = TaiKhoan(
            tendangnhap=tendangnhap,
            matkhau=matkhau,
            role_id=role_id
        )
        taikhoan.save()
        return taikhoan

    @classmethod
    def get_detail_taikhoan(cls, id: int):
        try:
            taikhoan = TaiKhoan.objects.get(pk=id)
        except Exception:
            return None
        return taikhoan

    @classmethod
    def put_taikhoan(cls, id: int, tendangnhap: str, matkhau: str, role_id: int):
        taikhoan = TaiKhoan.objects.get(pk=id)
        taikhoan.tendangnhap = tendangnhap
        taikhoan.matkhau = matkhau
        taikhoan.role_id = role_id
        taikhoan.save()
        return taikhoan

    @classmethod
    def delete_taikhoan(cls, id: int):
        taikhoan = TaiKhoan.objects.get(pk=id)
        return taikhoan.delete()
