from django.urls import path
from .views import TestView, NextDayTimePointView

urlpatterns = [
    path('get_next_day_and_sleep_seconds', NextDayTimePointView.as_view()),
    path('get_test_response', TestView.as_view()),
]
