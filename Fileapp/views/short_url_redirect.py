import falcon

from Fileapp.models.url_shortner import URL
from Fileapp.utils.response_handler.response_handler import ResponseEngine


class URLRedirect:

    def on_get(self, request, response, *args, **kwargs):
        url_key = kwargs.get('url_key')
        url = URL.objects.filter(uuid=url_key).first()
        if not url:
            return ResponseEngine(response=response, body='URL not found').error_response()
        response.status = falcon.HTTP_303
        response.set_header('Location', url.target_url)
        return response
