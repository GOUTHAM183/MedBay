from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    SchemeDetailView,
    )

urlpatterns = [
    path("", views.landing, name="landing"),
    path("home/", PostListView.as_view(), name="home"),
    path("schemes/", views.schemes, name="schemes"),
    path("map/", views.map, name="map"),
    path("scheme/<int:pk>/", SchemeDetailView.as_view(), name="scheme-detail"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("search/", views.search, name="search"),
    path("speech_to_text/",views.speech_to_text,name='speech_to_text'),
    path("location/",views.location,name='location'),
    ]