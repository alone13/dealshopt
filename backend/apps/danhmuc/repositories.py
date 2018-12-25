from typing import Optional

from backend.apps.danhmuc.models import DanhMuc


class DanhMucRepository(object):
    @classmethod
    def get_danhmuc_list(cls, limit: Optional[int] = None,
                         offset: Optional[int] = None,
                         sort: Optional[str] = None,
                         ):
        danhmuc_qs = DanhMuc.objects.values()

        total_count = len(danhmuc_qs)

        results = danhmuc_qs
        return results, total_count

    @classmethod
    def post_danhmuc(cls, danhmuccha: int, tendanhmuc: str, link: str, trangthai: bool):
        danhmuc = DanhMuc(
            danhmuccha=danhmuccha,
            tendanhmuc=tendanhmuc,
            link=link,
            trangthai=trangthai
        )
        danhmuc.save()
        return danhmuc

    @classmethod
    def get_detail_danhmuc(cls, id: int):
        try:
            danhmuc = DanhMuc.objects.get(pk=id)
        except Exception:
            return None
        return danhmuc

    @classmethod
    def put_danhmuc(cls, id: int, danhmuccha: int, tendanhmuc: str, link: str, trangthai: bool):
        danhmuc = DanhMuc.objects.get(pk=id)
        danhmuc.danhmuccha = danhmuccha
        danhmuc.tendanhmuc = tendanhmuc
        danhmuc.link = link
        danhmuc.trangthai = trangthai
        danhmuc.save()
        return danhmuc

    @classmethod
    def delete_danhmuc(cls, id: int):
        danhmuc = DanhMuc.objects.get(pk=id)
        return danhmuc.delete()
