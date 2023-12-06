from django.urls import path
from .views import PerkDetail, Perks, Experiences, ExperienceDetail, ExperiencePerks

urlpatterns = [
    path("", Experiences.as_view()),
    path("<int:pk>", ExperienceDetail.as_view()),
    path("<int:pk>/perks", ExperiencePerks.as_view()),
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkDetail.as_view()),
]
