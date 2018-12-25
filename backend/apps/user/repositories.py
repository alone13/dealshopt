from typing import Optional

from backend.apps.user.models import User, User_CuaHang_SanPham, User_TrangThai


class User_TrangThaiRepository(object):
    @classmethod
    def get_user_trangthai_list(cls, limit: Optional[int] = None,
                                offset: Optional[int] = None,
                                sort: Optional[str] = None,
                                ):
        user_trangthai_qs = User_TrangThai.objects.values()

        total_count = len(user_trangthai_qs)

        results = user_trangthai_qs
        return results, total_count

    @classmethod
    def post_user_trangthai(cls, trangthai: bool):
        user_trangthai = User_TrangThai(trangthai=trangthai)
        user_trangthai.save()
        return user_trangthai

    @classmethod
    def get_detail_user_trangthai(cls, id: int):
        try:
            user_trangthai = User_TrangThai.objects.get(pk=id)
        except Exception:
            return None
        return user_trangthai

    @classmethod
    def put_user_trangthai(cls, id: int, trangthai: bool):
        user_trangthai = User_TrangThai.objects.get(pk=id)
        user_trangthai.trangthai = trangthai
        user_trangthai.save()
        return user_trangthai

    @classmethod
    def delete_user_trangthai(cls, id: int):
        user_trangthai = User_TrangThai.objects.get(pk=id)
        return user_trangthai.delete()


class UserRepository(object):
    @classmethod
    def get_user_list(cls, limit: Optional[int] = None,
                      offset: Optional[int] = None,
                      sort: Optional[str] = None,
                      ):
        user_qs = User.objects.values()

        total_count = len(user_qs)

        results = user_qs
        return results, total_count

    @classmethod
    def post_user(cls, taikhoan_id: int, user_trangthai_id: int):
        user = User(taikhoan_id=taikhoan_id, user_trangthai_id=user_trangthai_id)
        user.save()
        return user

    @classmethod
    def get_detail_user(cls, id: int):
        try:
            user = User.objects.get(pk=id)
        except Exception:
            return None
        return user

    @classmethod
    def put_user(cls, id: int, taikhoan_id: int, user_trangthai_id: int):
        user = User.objects.get(pk=id)
        user.taikhoan_id = taikhoan_id
        user.user_trangthai_id = user_trangthai_id
        user.save()
        return user

    @classmethod
    def delete_user(cls, id: int):
        user = User.objects.get(pk=id)
        return user.delete()


class User_CuaHang_SanPhamRepository(object):
    @classmethod
    def get_user_cuahang_list(cls, limit: Optional[int] = None,
                              offset: Optional[int] = None,
                              sort: Optional[str] = None,
                              ):
        user_cuahang_qs = User_CuaHang_SanPham.objects.values()

        total_count = len(user_cuahang_qs)

        results = user_cuahang_qs
        return results, total_count

    @classmethod
    def post_user_cuahang(cls, user_id: int, sanpham_id: int, tencuahang: str):
        user_cuahang = User_CuaHang_SanPham(
            user_id=user_id,
            sanpham_id=sanpham_id,
            tencuahang=tencuahang
        )
        user_cuahang.save()
        return user_cuahang

    @classmethod
    def get_detail_user_cuahang(cls, id: int):
        try:
            user_cuahang = User_CuaHang_SanPham.objects.get(pk=id)
        except Exception:
            return None
        return user_cuahang

    @classmethod
    def put_user_cuahang(cls, id: int, user_id: int, sanpham_id: int, tencuahang: str):
        user_cuahang = User_CuaHang_SanPham.objects.get(pk=id)
        user_cuahang.user_id = user_id
        user_cuahang.sanpham_id = sanpham_id
        user_cuahang.tencuahang = tencuahang
        user_cuahang.save()
        return user_cuahang

    @classmethod
    def delete_user_cuahang(cls, id: int):
        user_cuahang = User_CuaHang_SanPham.objects.get(pk=id)
        return user_cuahang.delete()
