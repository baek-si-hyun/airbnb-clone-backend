from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.URLField()
    description = models.CharField(max_length=140)
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    file = models.URLField()
    # OneToOneField()는 반드시 하나의 데이터만 가질수 있게 해준다
    experience = models.OneToOneField(
        "experiences.Experience", on_delete=models.CASCADE, related_name="videos"
    )

    def __str__(self):
        return "Video File"
