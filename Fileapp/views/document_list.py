from falcon import before

from Fileapp.models.document import Document
from Fileapp.utils.auth.verify_token import login_required
from Fileapp.utils.response_handler.response_handler import ResponseEngine


class DocumentList:
    @before(login_required)
    def on_get(self, request, response):
        try:
            documents = Document.objects.filter(user=request.context.user_id)
            response_body = {}
            items = []
            for item in documents:
                items.append(item.to_dict)
            response_body['items'] = items
            return ResponseEngine(response=response, body=response_body).success_response()
        except FileNotFoundError:
            return ResponseEngine(response=response, body='No Documents Found').error_response()
