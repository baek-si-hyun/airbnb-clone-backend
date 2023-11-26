from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=15, choices=CategoryKindChoices.choices)

    # .title()은 첫글자를 대문자로 해준다
    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"
    # verbose_name_plural는 잘못 표기되는 문자열을 고쳐준다
    class Meta:
        verbose_name_plural = "Categories"
