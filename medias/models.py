from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(max_length=140)
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, null=True, blank=True
    )
    experience = models.ForeignKey(
        "experiences.Experience", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    file = models.FileField()
    # OneToOneField()는 반드시 하나의 데이터만 가질수 있게 해준다
    experience = models.OneToOneField(
        "experiences.Experience", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Video File"
