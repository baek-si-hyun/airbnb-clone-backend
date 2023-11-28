from django.contrib import admin
from .models import Room, Amenity


# @admin.action 은 관리자가 선택한 항목들을 일괄처리할수 있는 기능을 만들떄 쓰인다
# 3개의 매개변수를 받는데 첫번쨰는 actions = (reset_prices,)을 가지고 있는 모델(연결), 두번째는 해당 옵션을 사용하는 사용자가 누구인지, 세번째는 해당 모델의 데이터를 가져오는 quertset을 가져온다
@admin.action(description="Set all price to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
    list_display: (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )
    list_filter: (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    search_fields: {"owner__username"}
    # search_fields: {"^name"} 입력한 name으로 시작하는 name을 가진 리스트들을 검색
    # search_fields: {"=name"} 입력한 name과 완전히 똑같은 name을 가진 리스트들을 검색
    # search_fields: {"name"} 입력한 name이 포함되어 있는 name을 가진 리스트들을 검색
    # search_fields: {"owner__username"} 입력한 username이 포함되어 있는 owner를 가진 리스트들을 검색


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display: ("name", "description", "created_at", "updated_at")
    readonly_fields: ("created_at", "updated_at")
