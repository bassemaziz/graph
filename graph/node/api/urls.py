from django.urls import path

from .views import ConnectNodeAPI, GetShortestPathAPI

urlpatterns = [
    path("connect-node", ConnectNodeAPI.as_view(), name="connect_node"),
    path("path", GetShortestPathAPI.as_view(), name="path"),
]
