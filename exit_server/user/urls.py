from django.urls import path, include
from .views import (
    ClientLoginView,
    CounselorLoginView,
    ClientRegisterationView,
    CounselorRegisterationView,
    UserView,
    AbleTimeView,
)

urlpatterns = [
    path("counselor/sign-up/", CounselorRegisterationView.as_view()),
    path("client/sign-up/", ClientRegisterationView.as_view()),
    path("counselor/login/", CounselorLoginView.as_view()),
    path("client/login/", ClientLoginView.as_view()),
    path("counselor/", UserView.as_view()),
    path("able-time/<str:uid>", AbleTimeView.as_view()),
]