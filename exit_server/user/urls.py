from django.urls import path, include
from .views import (
    ClientLoginView,
    CounselorLoginView,
    ClientRegisterationView,
    CounselorRegisterationView,
    UserView,
)

urlpatterns = [
    path("counselor/sign-up/", CounselorRegisterationView.as_view()),
    path("client/sign-up/", ClientRegisterationView.as_view()),
    path("counselor/login/", CounselorLoginView.as_view()),
    path("client/login/", ClientLoginView.as_view()),
    path("counselor/<uid>", UserView.as_view()),
]