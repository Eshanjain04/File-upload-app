import random
import string as s
from falcon import before
from Fileapp.utils.auth.verify_token import login_required
from Fileapp.utils.response_handler.response_handler import ResponseEngine
from Fileapp.views.s3_manager import S3Manager
from Fileapp.models.document import Document


class DocUpload:  # API to handle Document upload to S3 and store document information in db
    @before(login_required)
    def on_post(self, request, response):
        for part in request.get_media():
            if not part.name == 'document':
                return ResponseEngine(response=response, body='File not found').error_response()
            uploaded_file = part
            path = S3Manager().upload_file(stream=uploaded_file.stream,
                                           file_name=uploaded_file.secure_filename,
                                           upload_location='fileuploadapp',
                                           is_public=True)  # return filename if successfully uploaded to s3
            random_value = ''.join(random.choices(s.ascii_uppercase + s.digits + s.ascii_lowercase, k=4))
            short_url = f'eshgetfile/{random_value}'  # short url for our file
            document = Document(
                file_name=uploaded_file.secure_filename,
                file_path=f'https://fileuploadappesh.s3.ap-south-1.amazonaws.com/{path}',
                file_type=uploaded_file.content_type,
                short_url=short_url,
                user=request.context.user_id
            ).save()  # storing document data in mongodb
            response_body = {
                'document': {'file': f'https://fileuploadappesh.s3.ap-south-1.amazonaws.com/{path}',
                             'short_url': short_url,
                             'id': str(document.pk)
                             }
            }
            return ResponseEngine(body=response_body, response=response).success_response()
