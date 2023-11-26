from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract는 해당 모델에 대한 테이블을 데이터베이스가 만들지 않게 해준다 (데이터베이스를 만들지 않고 참조만 함)
        abstract = True
