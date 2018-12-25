from backend.apps.base.mappers import NoContentResponseSchema
from backend.apps.base.views import BaseView
from backend.apps.danhmuc.logics import (
    DanhMucLogic
)
from backend.apps.danhmuc.mappers import (
    GetDanhMucListRequestSchema,
    GetDanhMucListResponseSchema,
    PostDanhMucRequestSchema,
    DanhMucResponseSchema,
    GetDanhMucRequestSchema,
    PutDanhMucRequestSchema,
    DeleteDanhMucRequestSchema
)
#import pdb;pdb.set_trace()

class DanhMucView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetDanhMucListRequestSchema(),
            response_schema=GetDanhMucListResponseSchema(),
            logic_method=DanhMucLogic.get_danhmuc_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostDanhMucRequestSchema(),
            response_schema=DanhMucResponseSchema(),
            logic_method=DanhMucLogic.post_danhmuc
        )


class DanhMucDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetDanhMucRequestSchema(),
            response_schema=DanhMucResponseSchema(),
            logic_method=DanhMucLogic.get_danhmuc,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutDanhMucRequestSchema(),
            response_schema=DanhMucResponseSchema(),
            logic_method=DanhMucLogic.put_danhmuc,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteDanhMucRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=DanhMucLogic.delete_danhmuc,
            code=id
        )
