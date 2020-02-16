import boto3

from django.conf import settings


def _get_client(service):
    return boto3.client(
        service,
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
        region_name=settings.AWS_REGION,
    )


def upload_file_to_s3(image, file_name, bucket):
    client = _get_client(service='s3')
    client.upload_fileobj(image, bucket, file_name)


def get_signed_urls_from_s3_object(file_name, bucket):
    client = _get_client(service='s3')

    return client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': file_name,
        },
    )


def detect_labels_from_image_using_aws_rekognition(photo, bucket):
    client = _get_client(service='rekognition')

    image = {
        'S3Object': {
            'Bucket': bucket,
            'Name': photo,
        },
    }

    response = client.detect_labels(Image=image)
    return response['Labels']
