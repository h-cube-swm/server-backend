from django.urls import path
from django.urls import include
from .views import RootView, ElementView

urlpatterns = [
    path("", RootView.as_view()),
    path("<int:user_pk>/", ElementView.as_view()),
    path("<int:user_pk>/surveys/", include("surveys.urls")),
]
