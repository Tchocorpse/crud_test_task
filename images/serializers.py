from rest_framework import serializers

from images.models import Image, Commentary


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'id', 'hash_value', 'image_size',)
        read_only_fields = ('id', 'hash_value', 'image_size',)


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('image', 'text', 'id', 'hash_value',)
        read_only_fields = ('id', 'hash_value', 'image_size',)
