import random
import string as s
from botocore.exceptions import InvalidRegionError

from settings.config import AWS_ACCESS_KEY_ID, AWS_REGION_NAME
from settings.config import AWS_BUCKET_NAME
from settings.config import AWS_SECRET_ACCESS_KEY
import boto3 as boto3


class S3Manager:

    def __init__(self,
                 access_key=AWS_ACCESS_KEY_ID,
                 secret_key=AWS_SECRET_ACCESS_KEY,
                 bucket=AWS_BUCKET_NAME,
                 region=AWS_REGION_NAME,
                 ):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket = bucket
        self.region = region
        self.upload_path = 'fileuploadapp'
        self.client = self.connection()

    def connection(self):
        _session = boto3.Session(region_name=self.region)
        try:
            return _session.client('s3',
                                   region_name=self.region,
                                   aws_access_key_id=self.access_key,
                                   aws_secret_access_key=self.secret_key
                                   )
        except InvalidRegionError:
            raise EnvironmentError('invalid region name')

    def upload_file(self, stream,
                    file_name,
                    upload_location,
                    is_public=False):
        extra_args = {}

        if is_public:
            extra_args = {'ACL': 'public-read'}

        s3_file_name = f'{self.upload_path}/{upload_location}/{self.get_file_name(file_name=file_name)}'

        self.client.upload_fileobj(stream, self.bucket, s3_file_name, ExtraArgs=extra_args)
        return s3_file_name

    @classmethod
    def get_file_name(cls, file_name):
        random_value = ''.join(random.choices(s.ascii_uppercase + s.digits + s.ascii_lowercase, k=10))
        return f'{random_value}-{file_name}'
