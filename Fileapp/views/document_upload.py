from falcon import before
import boto3 as boto3
from Fileapp.utils.auth.verify_token import login_required
from Fileapp.utils.response_handler.response_handler import ResponseEngine
from Fileapp.views.s3_manager import S3Manager
from settings.config import AWS_ACCESS_KEY_ID, AWS_REGION_NAME
from settings.config import AWS_BUCKET_NAME
from settings.config import AWS_SECRET_ACCESS_KEY
from Fileapp.models.document import Document


class DocUpload:
    @before(login_required)
    def on_post(self, request, response):
        for part in request.get_media():
            if not part.name == 'document':
                return ResponseEngine(response=response, body='File not found').error_response()
            uploaded_file = part
            path = S3Manager().upload_file(stream=uploaded_file.stream,
                                           file_name=uploaded_file.secure_filename,
                                           upload_location='fileuploadapp',
                                           is_public=True)
            document = Document(
                file_path=path,
                file_type=uploaded_file.content_type,
                user=request.context.user_id
            ).save()

            response_body = {
                'document': {'file': f'https://fileuploadappesh.s3.ap-south-1.amazonaws.com/{path}',
                             'id': str(document.pk)
                             }
            }
            return ResponseEngine(body=response_body, response=response).success_response()

