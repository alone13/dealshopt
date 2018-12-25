from backend.apps.base.mappers import NoContentResponseSchema
from backend.apps.base.views import BaseView
from backend.apps.taikhoan.logics import TaiKhoanLogic
from backend.apps.taikhoan.mappers import (
    GetTaiKhoanListRequestSchema,
    GetTaiKhoanListResponseSchema,
    PostTaiKhoanRequestSchema,
    TaiKhoanResponseSchema,
    GetTaiKhoanRequestSchema,
    PutTaiKhoanRequestSchema,
    DeleteTaiKhoanRequestSchema
)


class TaiKhoanView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetTaiKhoanListRequestSchema(),
            response_schema=GetTaiKhoanListResponseSchema(),
            logic_method=TaiKhoanLogic.get_taikhoan_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostTaiKhoanRequestSchema(),
            response_schema=TaiKhoanResponseSchema(),
            logic_method=TaiKhoanLogic.post_taikhoan
        )


class TaiKhoanDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetTaiKhoanRequestSchema(),
            response_schema=TaiKhoanResponseSchema(),
            logic_method=TaiKhoanLogic.get_taikhoan,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutTaiKhoanRequestSchema(),
            response_schema=TaiKhoanResponseSchema(),
            logic_method=TaiKhoanLogic.put_taikhoan,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteTaiKhoanRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=TaiKhoanLogic.delete_taikhoan,
            code=id
        )
