from django.urls import include, path
from .views import UserListView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

urlpatterns = [
    path('',UserListView.as_view()),
    path('', include(routers.urls)),
]