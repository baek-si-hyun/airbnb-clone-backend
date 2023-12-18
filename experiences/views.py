from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied, ParseError
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from .models import Perk, Experience
from bookings.models import Booking
from rooms.models import Room
from .serializers import (
    PerkSerializer,
    ExperiencesSerializer,
    BookingsSerializer,
    ExperienceDetailSerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Perks(APIView):
    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(PerkSerializer(perk).data)
        else:
            return Response(serializer.errors)


class PerkDetail(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk, data=request.data, partial=True)
        if serializer.is_valid():
            updated_perk = serializer.save()
            return Response(PerkSerializer(updated_perk).data)
        else:
            Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class ExperiencePerks(APIView):
    def get(self, request, pk):
        experience = Experience.objects.get(pk=pk)
        perks = experience.perks.all()
        serializer = PerkSerializer(perks, many=True)
        return Response(serializer.data)


class Experiences(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_experiences = Experience.objects.all()
        serializer = ExperiencesSerializer(all_experiences, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperiencesSerializer(data=request.data)
        if serializer.is_valid():
            host_pk = request.user
            experience = serializer.save(host=host_pk)
            return Response(ExperiencesSerializer(experience).data)
        else:
            return Response(serializer.errors)


class ExperienceDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(
            experience, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(
            experience, data=request.data, partial=True
        )
        if serializer.is_valid():
            update_experience = serializer.save()
            return Response(ExperienceDetailSerializer(update_experience).data)
        else:
            Response(serializer.errors)

    def delete(self, request, pk):
        experience = self.get_object(pk)
        experience.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class ExperienceBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        experience = self.get_object(pk)
        bookings = experience.bookings.all()
        serializer = BookingsSerializer(
            bookings, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = BookingsSerializer(data=request.data)
        if serializer.is_valid():
            room_pk = request.data.get("room")
            if not room_pk:
                raise ParseError("Room is required.")
            try:
                room = Room.objects.get(pk=room_pk)
                booking = serializer.save(
                    user=request.user,
                    experience=self.get_object(pk),
                    room=room,
                )
                serializer = BookingsSerializer(booking)
                return Response(serializer.data, status=HTTP_201_CREATED)
            except Exception:
                return Response(status=HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
