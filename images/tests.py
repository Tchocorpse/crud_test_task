import logging
import os

from rest_framework.test import APITestCase
from images.models import Image, Commentary


class GetStatTest(APITestCase):
    def setUp(self):

        self.url_pattern = "http://0.0.0.0:8000/stat/"
        self.test_num = 3
        self.mock_image_count = 1
        self.images = self.create_images(self.test_num)
        self.comments = self.create_comments(self.images, self.test_num)

    def create_images(self, n):
        image_list = []
        cur_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(cur_path, "Test_image.png")
        for i in range(n):
            image = Image(image=file_path)
            image_list.append(image)
            image.save()
        return image_list

    def create_comments(self, images, n):
        comments_list = []
        for image in images:
            for i in range(n):
                comment = Commentary(image=image, text=f"commentary {i}")
                comments_list.append(comment)
                comment.save()
        return comments_list

    def test_correct_operation(self):
        response = self.client.get(self.url_pattern)

        occupied_volume_raw = 0
        for image in self.images:
            occupied_volume_raw += image.image_size
        occupied_volume = round(occupied_volume_raw / 1048576, 3)

        test_dict = {
            "images_count": self.test_num,
            "unique_images_count": self.mock_image_count,
            "occupied_volume": occupied_volume,
            "comment_count": self.test_num * self.test_num,
            "unique_comment_count": self.test_num * self.mock_image_count,
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), test_dict)
