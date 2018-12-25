from typing import Optional
from backend.apps.admin.models import (
    Admin,
    Role,
    Module,
    Role_Module,
    HoatDong,
    Module_HoatDong
)


class AdminRepository(object):
    @classmethod
    def get_admin_list(cls, limit: Optional[int] = None,
                       offset: Optional[int] = None,
                       sort: Optional[str] = None,
                       ):
        admin_qs = Admin.objects.values()

        total_count = len(admin_qs)

        results = admin_qs
        return results, total_count

    @classmethod
    def post_admin(cls, taikhoan_id: int):
        admin = Admin(taikhoan_id=taikhoan_id)
        admin.save()
        return admin

    @classmethod
    def get_detail_admin(cls, id: int):
        try:
            admin = Admin.objects.get(pk=id)
        except Exception:
            return None
        return admin

    @classmethod
    def put_admin(cls, id: int, taikhoan_id: int):
        admin = Admin.objects.get(pk=id)
        admin.taikhoan_id = taikhoan_id
        admin.save()
        return admin

    @classmethod
    def delete_admin(cls, id: int):
        admin = Admin.objects.get(pk=id)
        return admin.delete()


class RoleRepository(object):
    @classmethod
    def get_role_list(cls, limit: Optional[int] = None,
                      offset: Optional[int] = None,
                      sort: Optional[str] = None,
                      ):
        role_qs = Role.objects.values()

        total_count = len(role_qs)

        results = role_qs
        return results, total_count

    @classmethod
    def post_role(cls, ten: str):
        role = Role(ten=ten)
        role.save()
        return role

    @classmethod
    def get_detail_role(cls, id: int):
        try:
            role = Role.objects.get(pk=id)
        except Exception:
            return None
        return role

    @classmethod
    def put_role(cls, id: int, ten: str):
        role = Role.objects.get(pk=id)
        role.ten = ten
        role.save()
        return role

    @classmethod
    def delete_role(cls, id: int):
        role = Role.objects.get(pk=id)
        return role.delete()


class ModuleRepository(object):
    @classmethod
    def get_module_list(cls, limit: Optional[int] = None,
                        offset: Optional[int] = None,
                        sort: Optional[str] = None,
                        ):
        module_qs = Module.objects.values()

        total_count = len(module_qs)

        results = module_qs
        return results, total_count

    @classmethod
    def post_module(cls, ten: str):
        module = Module(ten=ten)
        module.save()
        return module

    @classmethod
    def get_detail_module(cls, id: int):
        try:
            module = Module.objects.get(pk=id)
        except Exception:
            return None
        return module

    @classmethod
    def put_module(cls, id: int, ten: str):
        module = Module.objects.get(pk=id)
        module.ten = ten
        module.save()
        return module

    @classmethod
    def delete_module(cls, id: int):
        module = Module.objects.get(pk=id)
        return module.delete()


class Role_ModuleRepository(object):
    @classmethod
    def get_permission_list(cls, limit: Optional[int] = None,
                            offset: Optional[int] = None,
                            sort: Optional[str] = None,
                            ):
        permission_qs = Role_Module.objects.values()

        total_count = len(permission_qs)

        results = permission_qs
        return results, total_count

    @classmethod
    def post_permission(cls, module_id: int, role_id: int):
        permission = Role_Module(module_id=module_id, role_id=role_id)
        permission.save()
        return permission

    @classmethod
    def get_detail_permission(cls, id: int):
        try:
            permission = Role_Module.objects.get(pk=id)
        except Exception:
            return None
        return permission

    @classmethod
    def put_permission(cls, id: int, module_id: int, role_id: int):
        permission = Role_Module.objects.get(pk=id)
        permission.module_id = module_id
        permission.role_id = role_id
        permission.save()
        return permission

    @classmethod
    def delete_permission(cls, id: int):
        permission = Role_Module.objects.get(pk=id)
        return permission.delete()


class HoatDongRepository(object):
    @classmethod
    def get_hoatdong_list(cls, limit: Optional[int] = None,
                          offset: Optional[int] = None,
                          sort: Optional[str] = None,
                          ):
        hoatdong_qs = HoatDong.objects.values()

        total_count = len(hoatdong_qs)

        results = hoatdong_qs
        return results, total_count

    @classmethod
    def post_hoatdong(cls, ten: str):
        hoatdong = HoatDong(ten=ten)
        hoatdong.save()
        return hoatdong

    @classmethod
    def get_detail_hoatdong(cls, id: int):
        try:
            hoatdong = HoatDong.objects.get(pk=id)
        except Exception:
            return None
        return hoatdong

    @classmethod
    def put_hoatdong(cls, id: int, ten: str):
        hoatdong = HoatDong.objects.get(pk=id)
        hoatdong.ten = ten
        hoatdong.save()
        return hoatdong

    @classmethod
    def delete_hoatdong(cls, id: int):
        hoatdong = HoatDong.objects.get(pk=id)
        return hoatdong.delete()


class Module_HoatDongRepository(object):
    @classmethod
    def get_module_hoatdong_list(cls, limit: Optional[int] = None,
                                 offset: Optional[int] = None,
                                 sort: Optional[str] = None,
                                 ):
        module_hoatdong_qs = Module_HoatDong.objects.values()

        total_count = len(module_hoatdong_qs)

        results = module_hoatdong_qs
        return results, total_count

    @classmethod
    def post_module_hoatdong(cls, module_id: int, hoatdong_id: int):
        module_hoatdong = Module_HoatDong(module_id=module_id, hoatdong_id=hoatdong_id)
        module_hoatdong.save()
        return module_hoatdong

    @classmethod
    def get_detail_module_hoatdong(cls, id: int):
        try:
            module_hoatdong = Module_HoatDong.objects.get(pk=id)
        except Exception:
            return None
        return module_hoatdong

    @classmethod
    def put_module_hoatdong(cls, id: int, module_id: int, hoatdong_id: int):
        module_hoatdong = HoatDong.objects.get(pk=id)
        module_hoatdong.module_id = module_id
        module_hoatdong.hoatdong_id = hoatdong_id
        module_hoatdong.save()
        return module_hoatdong

    @classmethod
    def delete_module_hoatdong(cls, id: int):
        module_hoatdong = Module_HoatDong.objects.get(pk=id)
        return module_hoatdong.delete()
