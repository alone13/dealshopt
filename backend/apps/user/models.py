from django.db.models import (
    Model,
    AutoField,
    IntegerField,
    ForeignKey,
    CharField,
    BooleanField
)

class User_TrangThai(Model):
    id = AutoField("Id", primary_key=True)
    trangthai = BooleanField("TrangThai")

    class Meta:
        db_table = "User_TrangThai"

class User(Model):
    id = AutoField("Id", primary_key=True)
    taikhoan_id = IntegerField("TaiKhoan_Id")
    user_trangthai_id= ForeignKey(User_TrangThai,on_delete=User_TrangThai)

    class Meta:
        db_table = 'User'


class User_CuaHang_SanPham(Model):
    id = AutoField("Id", primary_key=True)
    user_id = ForeignKey(User,on_delete=User)
    sanpham_id = IntegerField("SanPham_Id")
    tencuahang = CharField("TenCuaHang", max_length=265)

    class Meta:
        db_table = "User_CuaHang_SanPham"
