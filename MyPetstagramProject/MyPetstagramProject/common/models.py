from django.contrib.auth import get_user_model
from django.db import models
from MyPetstagramProject.photos.models import Photo


UserModel = get_user_model()


class PhotoComment(models.Model):
    MEX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MEX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
