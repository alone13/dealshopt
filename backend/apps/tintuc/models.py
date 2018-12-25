from django.db.models import (
    Model,
    AutoField,
    CharField,
    BooleanField,
    IntegerField,
    DateField
)


class TinTuc(Model):
    id = AutoField("Id", primary_key=True)
    danhmuc_id = IntegerField("DanhMuc_Id")
    tieude = CharField("TieuDe", max_length=265)
    hinhanh = CharField("HinhAnh", max_length=265)
    mota = CharField("MoTa", max_length=265)
    noidung = CharField("NoiDung", max_length=265)
    ngaydang = DateField("NgayDang")
    trangthai = BooleanField("TrangThai")

    class Meta:
        db_table = 'TinTuc'
