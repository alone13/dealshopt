from django.conf import settings


class DomainManager(object):
    def __init__(self):
        self.app_domain = getattr(settings, 'DOMAIN_MAPPING', None)
        if not self.app_domain:
            raise Error("Missing DOMAIN_MAPPING")

        self.domain_app = {v.domain.lower(): k for k, v in self.app_domain.items()}

    def get_app(self, domain):
        return self.domain_app[domain]

    def get_domain_with_port(self, app):
        return self.app_domain[app].domain, self.app_domain[app].proxy_port
