from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    # filter의 제목을 정해야한다 (필수)
    title = "Filter by words"
    # filter의 기준을 정해야 한다 (필수)
    parameter_name = "word"

    # filter를 할 카테고리들을 만들어야한다. 반드시 리스트 형식 안에 튜플이 있는 구조여야한다. 튜플 왼쪽엔 필터링할 것, 오른쪽에는 admin 화면에 보여지는 필터버튼에 사용된다 (필수)
    def lookup(self, request, model_admin):
        return [("good", "Good"), ("great", "Great"), ("awesome", "Awesome")]

    # 어떻게 필터링을 할지 정하는 것이다 (필수)
    def queryset(self, request, reviews):
        # self.value()는 현재 선택된 필터 값("good", "great", "awesome")중 하나를 반환한다
        word = self.value()
        if word:
            # 선택한 필터 값(word)을 사용해 payload의 모델중에 word가 포함된(__contains) 목록을 가져온다
            return reviews.filter(payload__contains=word)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "payload")
    list_filter = ("rating", "user__is_host", "room__category", "room__pet_friendly")
