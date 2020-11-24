from django.urls import path, include
from .views import CreateReservationView

urlpatterns = [path("", CreateReservationView.as_view())]
