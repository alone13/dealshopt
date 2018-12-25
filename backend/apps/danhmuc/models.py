from django.db.models import (
    Model,
    AutoField,
    CharField,
    BooleanField,
    IntegerField
)


class DanhMuc(Model):
    id = AutoField("Id", primary_key=True)
    danhmuccha = IntegerField("DanhMucCha")
    tendanhmuc= CharField("TenDanhMuc", max_length=265)
    link= CharField("Link", max_length=265)
    trangthai= BooleanField("TrangThai")

    class Meta:
        db_table = 'DanhMuc'