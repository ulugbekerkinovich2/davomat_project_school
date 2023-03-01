from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from basic_app import views

urlpatterns = [
    path('user/', views.ListUsers.as_view()),
    path('user/<int:pk>', views.DetailUsers.as_view()),
    path('student/', views.ListStudent.as_view()),
    path('student/<int:pk>', views.DetailStudent.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
