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
    path('class/', views.ListSinf.as_view()),
    path('class/<int:pk>', views.DetailSinf.as_view()),
    path('daily/', views.ListBy_Day.as_view()),
    path('daily/<int:pk>', views.DetailBy_Day.as_view()),
    path('data/', views.List.as_view()),
    path('data/<int:pk>', views.Detail.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
