
class ApiError(Exception):
    """Raised if API returns something unexpected."""
    pass


class UpstreamApiError(ApiError):
    """Raised if the upstream API fails before returning usable JSON."""
    pass
