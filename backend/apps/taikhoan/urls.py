from django.urls import path
from backend.apps.taikhoan.views import(
    TaiKhoanView,
    TaiKhoanDetailView
)

urlpatterns = [
    path('', TaiKhoanView.as_view()),
    path('taikhoan/([0-9]+)/', TaiKhoanDetailView.as_view())
]
