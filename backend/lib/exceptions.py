class ResourceNotFoundException(Exception):
    pass


class RequestParameterException(Exception):
    pass


class UnauthenticatedException(Exception):
    pass


class IntegrityException(Exception):
    pass


class ForbiddenException(Exception):
    pass


class ConflictException(Exception):
    pass


class RollBackException(Exception):
    pass
