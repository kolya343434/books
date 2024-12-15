# myapp/storage_backends.py

from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'
    custom_domain = f"{settings.AWS_S3_ENDPOINT_URL}/{settings.AWS_STORAGE_BUCKET_NAME}/static"

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    custom_domain = f"{settings.AWS_S3_ENDPOINT_URL}/{settings.AWS_STORAGE_BUCKET_NAME}/media"
