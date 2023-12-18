from rest_framework.serializers import ModelSerializer
from .models import Perk, Experience
from bookings.models import Booking
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from rest_framework import serializers


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperiencesSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "name",
            "country",
            "city",
            "price",
            "date",
            "start",
            "end",
            "address",
            "description",
        )


class TinyExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = ("name",)


class BookingsSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class ExperienceDetailSerializer(ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    perks = PerkSerializer(read_only=True, many=True)
    bookings = BookingsSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    is_host = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "name",
            "country",
            "city",
            "price",
            "date",
            "start",
            "end",
            "address",
            "perks",
            "bookings",
            "category",
            "host",
            "is_host",
        )

    def get_is_host(self, host):
        request = self.context["request"]
        return host.name == request.user
