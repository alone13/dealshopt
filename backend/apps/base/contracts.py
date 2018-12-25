from typing import Optional
from urllib.parse import urlencode

COUNT_NAME = "count"
CURRENT_NAME = "current"
PREV_NAME = "prev"
NEXT_NAME = "next"
RESULTS_NAME = "results"
LIMIT_NAME = 'limit'
OFFSET_NAME = 'offset'
SORT_NAME = 'sort'

DEFAULT_LIMIT = 5
DEFAULT_OFFSET = 0
LATEST_UPDATED_SORT = 'latest-updated'
LATEST_ADDED_SORT = 'latest-added'


class PagingRequest(object):
    """Request
    """

    def __init__(self,
                 limit: int=DEFAULT_LIMIT,
                 offset: int=DEFAULT_OFFSET,
                 sort: Optional[str]=None):
        self.limit = limit
        self.offset = offset
        self.sort = sort


class PagingResponse(object):
    """Response
    """

    def __init__(self,
                 request_obj: PagingRequest,
                 path: str,
                 total_count: int):
        """
        Set HTTP Response parameter to Response object
        :param PagingRequest request_obj: Request parameters
        :param str path: Request path
        :param int total_count: return list count
        :return:
        """
        # Initialize
        self.count = total_count
        self.current = None
        self.prev = None
        self.next = None
        self.results = []
        # Calculate current, prev, next
        offset = request_obj.offset
        limit = request_obj.limit
        request_dict = {}
        for k, v in request_obj.__dict__.items():
            if isinstance(v, list):
                values = ','.join([str(item) for item in v])
                if values:
                    request_dict[k] = values
            elif v is not None:
                request_dict[k] = v

        self.current = path + '?' + urlencode(request_dict)
        next_offset = self._get_next_link(offset, limit, total_count)
        if next_offset:
            request_dict[OFFSET_NAME] = next_offset
            self.next = path + '?' + urlencode(request_dict)
        prev_offset = self._get_previous_link(offset, limit, total_count)
        if prev_offset is not None:
            request_dict[OFFSET_NAME] = prev_offset
            self.prev = path + '?' + urlencode(request_dict)

    @classmethod
    def _get_next_link(cls, offset, limit, total_count):
        if offset >= total_count or limit >= total_count:
            return None
        else:
            next_offset = limit + offset
            if next_offset >= total_count:
                return None
            else:
                return next_offset

    @classmethod
    def _get_previous_link(cls, offset, limit, total_count):
        if limit >= total_count or offset == 0:
            return None
        else:
            previous_offset = offset - limit
            if previous_offset < 0:
                previous_offset = 0
            return previous_offset


class NoContentResponse(object):
    pass
