import random
import string as s
from falcon import before

from Fileapp.models.url_shortner import URL
from Fileapp.utils.auth.verify_token import login_required
from Fileapp.utils.response_handler.response_handler import ResponseEngine
from Fileapp.views.s3_manager import S3Manager
from Fileapp.models.document import Document
from settings.config import AWS_S3_BASE_URL, BASE_URL_DEPLOY


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

            short_url = f'{BASE_URL_DEPLOY}/{random_value}'  # short url for our file
            file_url = f'{AWS_S3_BASE_URL}/{path}'
            document = Document.objects.filter(file_path=file_url).first()
            if document:
                return ResponseEngine(body='file Already Exists', response=response).error_response()
            document = Document(
                file_name=uploaded_file.secure_filename,
                file_path=file_url,
                file_type=uploaded_file.content_type,
                short_url=short_url,
                user=request.context.user_id
            ).save()  # storing document data in mongodb
            URL(target_url=file_url, uuid=random_value).save()
            response_body = {
                'document': {'file': f'{AWS_S3_BASE_URL}/{path}',
                             'short_url': short_url,
                             'id': str(document.pk)
                             }
            }
            return ResponseEngine(body=response_body, response=response).success_response()
