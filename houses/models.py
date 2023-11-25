from django.db import models

# House클래스에 장고에서 기본으로 제공해주는 models.Model을 상속받는다
# model을 데이터베이스와 통신하는 위한 로직을 말한다.
# model을 추가했으면 python manage.py makemigrations 을 통해 장고가 해당 모델을 데이터베이스에 적용할 수 있게 해주는 migration을 생성해야 하야한다.
# 생성된 migration을 db에게 알려주기 위해 python manage.py migrate 을 실행한다.


class House(models.Model):

    """House Model"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Positive Numbers Only"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True,
        help_text="Does this house allow pets?",
    )

    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return
