from django.utils.deprecation import MiddlewareMixin

CACHE_CONTROL_HEADER = 'no-cache, no-store, must-revalidate'
PRAGMA_HEADER = 'no-cache'
EXPIRES_HEADER = '0'


class NoCacheMiddleware(MiddlewareMixin):
    def process_response(self, request, http_response):
        http_response['Cache-Control'] = CACHE_CONTROL_HEADER
        http_response['Pragma'] = PRAGMA_HEADER
        http_response['Expires'] = EXPIRES_HEADER
        return http_response