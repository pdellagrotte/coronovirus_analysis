import logging
import boto3
import os
from botocore.exceptions import ClientError

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "\data"
BUCKET_NAME="amazing-paul-bucket-123"

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

s3 = boto3.client('s3')


print("Loading files to " + BUCKET_NAME)
for file in os.listdir(DATA_DIR):
    print("Loading " + file)
    with open(os.path.abspath(os.path.join(DATA_DIR, file)), "rb") as f:
        s3.upload_fileobj(f, BUCKET_NAME, file)

