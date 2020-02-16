from rest_framework.test import APITestCase, APIClient
from unittest import mock

from django.core.files import File


class ImageViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_images(self):
        response = self.client.get('/images/')

        assert response.status_code == 200
        assert response.data.get('count') == 0

    @mock.patch('imagedb.images.serializer.get_signed_urls_from_s3_object')
    @mock.patch('imagedb.images.models.detect_labels_from_image_using_aws_rekognition')
    @mock.patch('imagedb.images.models.upload_file_to_s3')
    def test_save(self, mock_file_upload, mock_detect_labels, mock_signed_url):
        file = File(open('uploads/1581464313/landscape_resized.jpg', 'rb'))
        mock_signed_url.return_value = 'test'
        mock_detect_labels.return_value = []

        response = self.client.post('/images/', {'image': file})

        assert mock_file_upload.called
        assert mock_detect_labels.called

        assert response.status_code == 201
        assert response.data.get('file_name') == 'landscape_resized.jpg'
        assert response.data.get('s3_url') == 'test'
        assert len(response.data.get('labels')) == 0

    @mock.patch('imagedb.images.serializer.get_signed_urls_from_s3_object')
    @mock.patch('imagedb.images.models.detect_labels_from_image_using_aws_rekognition')
    @mock.patch('imagedb.images.models.upload_file_to_s3')
    def test_save_with_labels(self, mock_file_upload, mock_detect_labels, mock_signed_url):
        file = File(open('uploads/1581464313/landscape_resized.jpg', 'rb'))
        mock_signed_url.return_value = 'test'
        mock_detect_labels.return_value = [{"Name": "test-name", "Confidence": 99}]

        response = self.client.post('/images/', {'image': file})

        assert mock_file_upload.called
        assert mock_detect_labels.called

        assert response.status_code == 201
        assert response.data.get('file_name') == 'landscape_resized.jpg'
        assert response.data.get('s3_url') == 'test'
        assert len(response.data.get('labels')) == 1
        assert response.data.get('labels')[0]['label'] == "test-name"
        assert response.data.get('labels')[0]['confidence'] == 99


class ImageLabelViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_image_labels(self):
        response = self.client.get('/imagelabels/')

        assert response.status_code == 200
        assert response.data.get('count') == 0
