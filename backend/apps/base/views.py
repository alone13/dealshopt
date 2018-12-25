import json
from typing import Callable, Optional
from marshmallow import Schema
from django.http import response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.lib.exceptions import (
    RequestParameterException,
    ResourceNotFoundException,
    ForbiddenException,
    ConflictException
)


class BaseView(APIView):
    def base_request(self,
                     request: Request,
                     request_schema: Schema,
                     response_schema: Schema,
                     logic_method: Callable[[object, Optional[str]], object],
                     is_paging: Optional[bool]=False,
                     code=None
                     ):
        request_obj, request_errors = self._request_schema(request, request_schema, code)
        if request_errors:
            return response.HttpResponseBadRequest(json.dumps(request_errors))

        response_data, response_errors = self._response_schema(request,
                                                               request_obj,
                                                               response_schema,
                                                               logic_method,
                                                               is_paging)
        if response_errors:
            if isinstance(response_errors, (str, dict)):
                return Response(response_errors, status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return response_errors

        if request.method == 'POST':
            return Response(response_data, status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            return Response({}, status.HTTP_204_NO_CONTENT)
        else:
            return Response(response_data, status.HTTP_200_OK)

    def _request_schema(self, request, request_schema, code=None):
        if not request:
            return {}, 'Not request'
        request_param = {}
        if request.query_params:
            request_param.update(self._convert_to_dict(request.query_params))
        if request.data:
            request_param.update(request.data)
        if code:
            request_param["id"] = code
        return request_schema.load(request_param)

    def _response_schema(self, request, request_obj, response_schema, logic_method, is_paging=False):
        try:
            if is_paging:
                path = self._parse_path(request)
                response_obj = logic_method(request_obj, path)
            else:
                response_obj = logic_method(request_obj)

        except RequestParameterException as e:
            return {}, response.HttpResponseBadRequest(content=e)
        except ResourceNotFoundException as e:
            return {}, response.HttpResponseNotFound(content=e)
        except ForbiddenException as e:
            return {}, response.HttpResponseForbidden(content=e)
        except ConflictException as e:
            return {}, response.HttpResponse(content=e, status=status.HTTP_409_CONFLICT)
        return response_schema.dump(response_obj)

    def _parse_path(self, request):
        return '{scheme}://{host}{path}'.format(
            scheme=request._get_scheme(),
            host=request.get_host(),
            path=request.path
        )

    def _convert_to_dict(self, querydict):
        converted_dict = dict()
        for key, item in querydict.items():
            splited_item = item.split(',')
            if len(splited_item) == 1:
                converted_dict[key] = splited_item[0]
            else:
                converted_dict[key] = splited_item

        return converted_dict
