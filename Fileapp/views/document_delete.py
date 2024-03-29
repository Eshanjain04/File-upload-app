from falcon import before

from Fileapp.models.document import Document
from Fileapp.utils.auth.verify_token import login_required
from Fileapp.utils.response_handler.response_handler import ResponseEngine


class DocumentDelete:
    @before(login_required)
    def on_delete(self, request, response, *args, **kwargs):
        item_id = kwargs.get('pk')
        response_body = {}
        try:
            document = Document.objects.filter(user=request.context.user_id, pk=item_id).first()
            if not document:
                response_body['status'] = 'failed'
                response_body['msg'] = 'File not found'
                return ResponseEngine(response=response, body=response_body).error_response()
            document.delete()
            response_body = {
                'status': 'success',
                'msg': 'Document Deleted Successfully'
            }
            return ResponseEngine(response=response, body=response_body).success_response()

        except FileNotFoundError:
            return ResponseEngine(response=response, body='No Documents Found').error_response()
