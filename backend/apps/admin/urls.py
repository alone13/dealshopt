from django.urls import path
"""from .import views"""
from backend.apps.admin.views import (
    AdminView,
    AdminDetailView,
    RoleView,
    RoleDetailView,
    ModuleView,
    ModuleDetailView,
    PermissionView,
    PermissionDetailView,
    HoatDongView,
    HoatDongDetailView,
    Module_HoatDongView,
    Module_HoatDongDetailView
)

urlpatterns = [
    #path('admin/', AdminView.as_view()),
    path('', AdminView.as_view()),
    path('admin/([0-9]+)/', AdminDetailView.as_view()),
    path('role/', RoleView.as_view()),
    path('role/([0-9]+)/', RoleDetailView.as_view()),
    path('module/', ModuleView.as_view()),
    path('module/([0-9]+)/', ModuleDetailView.as_view()),
    path('permission/', PermissionView.as_view()),
    path('permission/([0-9]+)/', PermissionDetailView.as_view()),
    path('action/', HoatDongView.as_view()),
    path('action/([0-9]+)/', HoatDongDetailView.as_view()),
    path('moduleaction/', Module_HoatDongView.as_view()),
    path('moduleaction/([0-9]+)/', Module_HoatDongDetailView.as_view())
]
