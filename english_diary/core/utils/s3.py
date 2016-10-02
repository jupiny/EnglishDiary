from django.conf import settings

from boto.s3.connection import S3Connection, Bucket, Key


def delete_file_from_s3(filename):
    conn = S3Connection(
        settings.AWS_ACCESS_KEY_ID,
        settings.AWS_SECRET_ACCESS_KEY,
    )
    b = Bucket(
        conn,
        settings.AWS_STORAGE_BUCKET_NAME,
    )
    k = Key(b)
    k.key = filename
    b.delete_key(k)
