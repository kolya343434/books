# myapp/storage_backends.py

from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    bucket_name = 'bookss'
    location = 'static'

class MediaStorage(S3Boto3Storage):
    bucket_name = 'bookss'
    location = 'media'
