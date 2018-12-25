from django.db.models import (
    Model,
    AutoField,
    CharField,
    IntegerField,
    ForeignKey
)


class Admin(Model):
    id = AutoField("Id", primary_key=True)
    taikhoan_id = IntegerField("TaiKhoan_Id")

    class Meta:
        db_table = 'Admin'


class Role(Model):
    id = AutoField("Id", primary_key=True)
    ten = CharField("Ten", max_length=265)

    class Meta:
        db_table = 'Role'


class Module(Model):
    id = AutoField("Id", primary_key=True)
    ten = CharField("Ten", max_length=265)

    class Meta:
        db_table = 'Module'


class Role_Module(Model):
    id = AutoField("Id", primary_key=True)
    module_id = ForeignKey(Module,on_delete=Module)
    role_id = ForeignKey(Role,on_delete=Role)

    class Meta:
        db_table = "Role_Module"


class HoatDong(Model):
    id = AutoField("Id", primary_key=True)
    ten = CharField("Ten", max_length=265)

    class Meta:
        db_table = 'HoatDong'


class Module_HoatDong(Model):
    id = AutoField("Id", primary_key=True)
    module_id = ForeignKey(Module,on_delete=Module)
    hoatdong_id = ForeignKey(HoatDong,on_delete=HoatDong)

    class Meta:
        db_table = "Module_HoatDong"
