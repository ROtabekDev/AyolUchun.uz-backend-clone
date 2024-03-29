from django.urls import path

from .views import (
    ContactCreateAPIView, NotificationListAPIView, 
    NotificationDetailAPIView, GetCertificateAPIView
)

urlpatterns = [
    path('create/contact/', ContactCreateAPIView.as_view()),
    path('notification/list/', NotificationListAPIView.as_view()),
    path('notification/detail/<str:slug>/', NotificationDetailAPIView.as_view()),
    path('certificate/get/<str:course_slug>/', GetCertificateAPIView.as_view()),
]