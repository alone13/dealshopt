from django.urls import path
from backend.apps.user.views import (
    UserView,
    UserDetailView,
    User_CuaHangView,
    User_CuaHangDetailView,
    User_TrangThaiView,
    User_TrangThaiDetailView
)

urlpatterns = [
    path('', UserView.as_view()),
    path('user/([0-9]+)/', UserDetailView.as_view()),
    path('user_cuahang/', User_CuaHangView.as_view()),
    path('user_cuahang/([0-9]+)/', User_CuaHangDetailView.as_view()),
    path('user_trangthai/', User_TrangThaiView.as_view()),
    path('user_trangthai/([0-9]+)/', User_TrangThaiDetailView.as_view())
]
