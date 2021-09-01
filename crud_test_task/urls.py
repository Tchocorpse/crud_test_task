from django.contrib import admin
from django.urls import path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions

from images.views import (
    CreateImage,
    UpdateImage,
    GetImages,
    DeleteImage,
    GetCommentaries,
    CreateCommentary,
    UpdateCommentary,
    DeleteCommentary, GetStat,
)

schema_view = get_schema_view(
   openapi.Info(
      title="API references",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("images/", GetImages.as_view()),
    path("images/create/", CreateImage.as_view()),
    path("images/update/<int:pk>/", UpdateImage.as_view()),
    path("images/delete/<int:pk>/", DeleteImage.as_view()),

    path("commentaries/", GetCommentaries.as_view()),
    path("commentaries/create/", CreateCommentary.as_view()),
    path("commentaries/update/<int:pk>/", UpdateCommentary.as_view()),
    path("commentaries/delete/<int:pk>/", DeleteCommentary.as_view()),

    path("stat/", GetStat.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
