from django.urls import path
from . import views

# .as_view()는 클래스 안의 함수들을 알맞은 상황에 맞게 실행해주는 메서드이다.
urlpatterns = [
    path("", views.Rooms.as_view()),
    path("<int:pk>", views.RoomDetail.as_view()),
    path("<int:pk>/reviews", views.RoomReviews.as_view()),
    path("<int:pk>/photos", views.RoomReviews.as_view()),
    path("<int:pk>/bookings", views.RoomBookings.as_view()),
    path("<int:pk>/bookings/check", views.RoomBookingCheck.as_view()),
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>", views.AmenityDetail.as_view()),
]
