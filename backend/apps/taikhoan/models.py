from django.db.models import (
    Model,
    AutoField,
    CharField,
    IntegerField
)


class TaiKhoan(Model):
    id = AutoField("Id", primary_key=True)
    tendangnhap = CharField("TenDN", max_length=265)
    matkhau = CharField("MatKhau", max_length=265)
    role_id = IntegerField("Role_Id")

    class Meta:
        db_table = 'TaiKhoan'
