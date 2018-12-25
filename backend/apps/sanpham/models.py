from django.db.models import (
    Model,
    AutoField,
    CharField,
    BooleanField,
    IntegerField,
    DateField,
    ForeignKey,
    FloatField
)


class TinhThanh(Model):
    id = AutoField("Id", primary_key=True)
    ten = CharField("Ten", max_length=265)
    trangthai = BooleanField("TrangThai")

    class Meta:
        db_table = 'TinhThanh'


class QuanHuyen(Model):
    id = AutoField("Id", primary_key=True)
    tinh_id = ForeignKey(TinhThanh,on_delete=TinhThanh)
    ten = CharField("Ten", max_length=265)
    trangthai = BooleanField("TrangThai")

    class Meta:
        db_table = 'QuanHuyen'


class SanPham_BaoMat(Model):
    id = AutoField("Id", primary_key=True)
    ten = CharField("Ten", max_length=265)

    class Meta:
        db_table = 'SanPham_BaoMat'


class SanPham_TrangThai(Model):
    id = AutoField("Id", primary_key=True)
    trangthai = BooleanField("TrangThai")

    class Meta:
        db_table = 'SanPham_TrangThai'


class AmThuc(Model):
    id = AutoField("Id", primary_key=True)
    ten = CharField("Ten", max_length=265)
    trangthai = BooleanField("TrangThai")

    class Meta:
        db_table = 'AmThuc'


class TheLoai_SanPham(Model):
    id = AutoField("Id", primary_key=True)
    ten = CharField("Ten", max_length=265)
    link = CharField("Link", max_length=265)
    trangthai = BooleanField("TrangThai")

    class Meta:
        db_table = 'TheLoai_SanPham'


class SanPham(Model):
    id = AutoField("Id", primary_key=True)
    user_cuahang_id=IntegerField("User_CuaHang")
    theloai_id=ForeignKey(TheLoai_SanPham,on_delete=TheLoai_SanPham)
    danhmuc_id=IntegerField("DanhMuc_Id")
    baomat_id=ForeignKey(SanPham_BaoMat,on_delete=SanPham_BaoMat)
    trangthai_id=ForeignKey(SanPham_TrangThai,on_delete=SanPham_TrangThai)
    amthuc_id=ForeignKey(AmThuc,on_delete=AmThuc)
    tinhthanh_id=ForeignKey(TinhThanh,on_delete=TinhThanh)
    quanhuyen_id=ForeignKey(QuanHuyen,on_delete=QuanHuyen)
    tensanpham=CharField("TenSanPham", max_length=265)
    hinhanh=CharField("HinhAnh", max_length=265)
    ngaydang=DateField("NgayDang")
    soluong=IntegerField("SoLuong")

    class Meta:
        db_table = 'SanPham'


class LuaChon_SanPham(Model):
    id = AutoField("Id", primary_key=True)
    sanpham_id = ForeignKey(SanPham,on_delete=SanPham)
    ten = CharField("Ten", max_length=265)

    class Meta:
        db_table = 'LuaChon_SanPham'


class SanPham_Gia(Model):
    id = AutoField("Id", primary_key=True)
    sanpham_id = ForeignKey(SanPham,on_delete=SanPham)

    class Meta:
        db_table = 'SanPham_Gia'


class SanPham_Gia_ChiTiet(Model):
    id = AutoField("Id", primary_key=True)
    sanpham_gia_id = ForeignKey(SanPham_Gia,on_delete=SanPham_Gia)
    gia=FloatField("Gia")
    ngaybd=DateField("NgayBatDau")
    ngaykt=DateField("NgayKetThuc")
    is_active=BooleanField("Active")

    class Meta:
        db_table = 'SanPham_Gia_ChiTiet'
