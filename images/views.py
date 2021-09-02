from django.db.models import Sum
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from images.models import Image, Commentary
from images.serializers import ImageSerializer, CommentarySerializer


class CreateImage(generics.CreateAPIView):
    serializer_class = ImageSerializer


class GetImages(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UpdateImage(generics.UpdateAPIView):
    queryset = Image.objects.all()
    lookup_field = "pk"
    serializer_class = ImageSerializer


class DeleteImage(generics.DestroyAPIView):
    queryset = Image.objects.all()
    lookup_field = "pk"
    serializer_class = ImageSerializer


class CreateCommentary(generics.CreateAPIView):
    serializer_class = CommentarySerializer


class GetCommentaries(generics.ListAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


class UpdateCommentary(generics.UpdateAPIView):
    queryset = Commentary.objects.all()
    lookup_field = "pk"
    serializer_class = CommentarySerializer


class DeleteCommentary(generics.DestroyAPIView):
    queryset = Commentary.objects.all()
    lookup_field = "pk"
    serializer_class = CommentarySerializer


class GetStat(APIView):
    @swagger_auto_schema(
        method="get",
        responses={
            status.HTTP_200_OK: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "images_count": openapi.Schema(
                        type=openapi.TYPE_NUMBER, description="Total number of images"
                    ),
                    "unique_images_count": openapi.Schema(
                        type=openapi.TYPE_NUMBER,
                        description="Total number of unique images",
                    ),
                    "comment_count": openapi.Schema(
                        type=openapi.TYPE_NUMBER,
                        description="Total number of commentaries",
                    ),
                    "unique_comment_count": openapi.Schema(
                        type=openapi.TYPE_NUMBER,
                        description="Total number of unique commentaries",
                    ),
                    "occupied_size": openapi.Schema(
                        type=openapi.TYPE_NUMBER, description="Occupied size in mb "
                    ),
                },
            ),
        },
    )
    @action(detail=False, methods=["GET"])
    def get(self, request):
        images_qs = Image.objects.all()
        images_count, unique_images_count = self._counting_machine(
            images_qs, "hash_value"
        )

        comments_qs = Commentary.objects.all()
        comment_count, unique_comment_count = self._counting_machine(
            comments_qs, "hash_value"
        )

        occupied_size = self.bytes_to_mb(self._measure_images_size(images_qs))

        result = {
            "images_count": images_count,
            "unique_images_count": unique_images_count,
            "occupied_size": occupied_size,
            "comment_count": comment_count,
            "unique_comment_count": unique_comment_count,
        }

        return Response(data=result, status=200)

    def _counting_machine(self, qs, unique_field):
        count = qs.count()
        unique_count = qs.distinct(unique_field).count()
        return count, unique_count

    def _measure_images_size(self, qs):
        return qs.aggregate(Sum("image_size"))["image_size__sum"]

    def bytes_to_mb(self, bts):
        return round(bts / 1048576, 3)
