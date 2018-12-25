from backend.lib.domain_manager import DomainManager
from logging import getLogger

logger = getLogger(__name__)


class DomainRoutingMiddleware(object):
    def __init__(self):
        self.domain_manager = DomainManager()

    def process_request(self, request):
        try:
            domain = request.get_host().split(':')[0].lower()
            app = self.domain_manager.get_app(domain)
            request.urlconf = 'backend.apps.{app}.urls'.format(app=app)
        except Exception as e:
            logger.warning(e)
