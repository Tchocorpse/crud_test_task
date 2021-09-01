from rest_framework import serializers

from images.models import Image, Commentary


class ImageSerializerWithId(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'id')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('image', 'text',)


class CommentarySerializerWithId(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('image', 'text', 'id')
