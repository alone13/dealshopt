from backend.apps.base.mappers import NoContentResponseSchema
from backend.apps.base.views import BaseView
from backend.apps.dathang.logics import KhachHangLogic, DonHangLogic, CTDonHangLogic
from backend.apps.dathang.mappers import (
    GetKhachHangListRequestSchema,
    GetKhachHangListResponseSchema,
    PostKhachHangRequestSchema,
    KhachHangResponseSchema,
    GetKhachHangRequestSchema,
    PutKhachHangRequestSchema,
    DeleteKhachHangRequestSchema,
    GetDonHangListRequestSchema, GetDonHangListResponseSchema, PostDonHangRequestSchema, DonHangResponseSchema,
    GetDonHangRequestSchema, PutDonHangRequestSchema, DeleteDonHangRequestSchema, GetCTDonHangRequestSchema,
    CTDonHangResponseSchema, GetCTDonHangListRequestSchema, GetCTDonHangListResponseSchema, PostCTDonHangRequestSchema,
    PutCTDonHangRequestSchema, DeleteCTDonHangRequestSchema)


class KhachHangView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetKhachHangListRequestSchema(),
            response_schema=GetKhachHangListResponseSchema(),
            logic_method=KhachHangLogic.get_khachhang_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostKhachHangRequestSchema(),
            response_schema=KhachHangResponseSchema(),
            logic_method=KhachHangLogic.post_khachhang
        )


class KhachHangDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetKhachHangRequestSchema(),
            response_schema=KhachHangResponseSchema(),
            logic_method=KhachHangLogic.get_khachhang,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutKhachHangRequestSchema(),
            response_schema=KhachHangResponseSchema(),
            logic_method=KhachHangLogic.put_khachhang,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteKhachHangRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=KhachHangLogic.delete_khachhang,
            code=id
        )


class DonHangView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetDonHangListRequestSchema(),
            response_schema=GetDonHangListResponseSchema(),
            logic_method=DonHangLogic.get_donhang_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostDonHangRequestSchema(),
            response_schema=DonHangResponseSchema(),
            logic_method=DonHangLogic.post_donhang
        )


class DonHangDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetDonHangRequestSchema(),
            response_schema=DonHangResponseSchema(),
            logic_method=DonHangLogic.get_donhang,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutDonHangRequestSchema(),
            response_schema=DonHangResponseSchema(),
            logic_method=DonHangLogic.put_donhang,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteDonHangRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=DonHangLogic.delete_donhang,
            code=id
        )


class CTDonHangView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetCTDonHangListRequestSchema(),
            response_schema=GetCTDonHangListResponseSchema(),
            logic_method=CTDonHangLogic.get_ctdonhang_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostCTDonHangRequestSchema(),
            response_schema=CTDonHangResponseSchema(),
            logic_method=CTDonHangLogic.post_ctdonhang
        )


class CTDonHangDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetCTDonHangRequestSchema(),
            response_schema=CTDonHangResponseSchema(),
            logic_method=CTDonHangLogic.get_ctdonhang,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutCTDonHangRequestSchema(),
            response_schema=CTDonHangResponseSchema(),
            logic_method=CTDonHangLogic.put_ctdonhang,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteCTDonHangRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=CTDonHangLogic.delete_ctdonhang,
            code=id
        )
