from django.urls import path
from backend.apps.dathang.views import(
    KhachHangView,
    KhachHangDetailView,
    DonHangView,
    DonHangDetailView,
    CTDonHangView,
    CTDonHangDetailView
)

urlpatterns = [
    path('', KhachHangView.as_view()),
    #path('khachhang/', KhachHangView.as_view()),
    path('khachhang/([0-9]+)/', KhachHangDetailView.as_view()),
    path('donhang/', DonHangView.as_view()),
    path('donhang/([0-9]+)/', DonHangDetailView.as_view()),
    path('chitietdonhang/', CTDonHangView.as_view()),
    path('chitietdonhang/([0-9]+)/', CTDonHangDetailView.as_view())
]
