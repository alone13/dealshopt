from backend.apps.base.mappers import NoContentResponseSchema
from backend.apps.base.views import BaseView
from backend.apps.tintuc.logics import TinTucLogic
from backend.apps.tintuc.mappers import (
    GetTinTucListRequestSchema,
    GetTinTucListResponseSchema,
    PostTinTucRequestSchema,
    TinTucResponseSchema,
    GetTinTucRequestSchema,
    PutTinTucRequestSchema,
    DeleteTinTucRequestSchema
)


class TinTucView(BaseView):
    def get(self, request):
        return self.base_request(
            request=request,
            request_schema=GetTinTucListRequestSchema(),
            response_schema=GetTinTucListResponseSchema(),
            logic_method=TinTucLogic.get_tintuc_list,
            is_paging=True
        )

    def post(self, request):
        return self.base_request(
            request=request,
            request_schema=PostTinTucRequestSchema(),
            response_schema=TinTucResponseSchema(),
            logic_method=TinTucLogic.post_tintuc
        )


class TinTucDetailView(BaseView):
    def get(self, request, id):
        return self.base_request(
            request=request,
            request_schema=GetTinTucRequestSchema(),
            response_schema=TinTucResponseSchema(),
            logic_method=TinTucLogic.get_tintuc,
            code=id
        )

    def put(self, request, id):
        return self.base_request(
            request=request,
            request_schema=PutTinTucRequestSchema(),
            response_schema=TinTucResponseSchema(),
            logic_method=TinTucLogic.put_tintuc,
            code=id
        )

    def delete(self, request, id):
        return self.base_request(
            request=request,
            request_schema=DeleteTinTucRequestSchema(),
            response_schema=NoContentResponseSchema(),
            logic_method=TinTucLogic.delete_tintuc,
            code=id
        )
