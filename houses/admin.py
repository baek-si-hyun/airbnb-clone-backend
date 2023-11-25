from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # admin 화면에 보여주고 싶은 form의 구조를 변경하는 로직
    # fields = (
    #     "name",
    #     "address",
    #     ("price_per_night", "pets_allowed"),
    # )
    # admin 화면에 보여주고 싶은 column를 정하는 로직
    # 해당 model(House)의 property들이여야 한다
    list_display = ("name", "price_per_night", "address", "pets_allowed")
    # admin 화면에 보여주고 싶은 filter목록을 정하는 로직
    list_filter = ("price_per_night", "pets_allowed")
    # admin 화면에서 검색의 기준을 정하는 로직
    # 뒤에 __startswith를 붙이면 검색한 글자로 시작하는 목록만 검색한다
    # search_fields = ("address",)
    # list_display_links = ("name", "address")
    # list_editable = ("pets_allowed",)