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


class KhachHang(Model):
    id = AutoField("Id", primary_key=True)
    tenkhachhang = CharField("TenKhachHang", max_length=265)
    diachi = CharField("DiaChi", max_length=265)
    email = CharField("Email", max_length=265)
    sdt = IntegerField("SDT")

    class Meta:
        db_table = 'KhachHang'


class DonHang(Model):
    id = AutoField("Id", primary_key=True)
    khachhang_id = ForeignKey(KhachHang,on_delete=KhachHang)
    ngaydat = DateField("NgayDat")
    trangthai = BooleanField("DonHang")

    class Meta:
        db_table = 'DonHang'


class CTDonHang(Model):
    id = AutoField("Id", primary_key=True)
    donhang_id = ForeignKey(DonHang,on_delete=DonHang)
    sanpham_id = IntegerField("SanPham")
    gia = FloatField("Gia")
    thanhtien = FloatField("ThanhTien")

    class Meta:
        db_table = 'CTDonHang'
