from django.urls import path
from .views import RootView, ElementView

urlpatterns = [
    path("", RootView.as_view()),
    path("<int:pk>/", ElementView.as_view()),
]
