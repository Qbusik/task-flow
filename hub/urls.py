from django.urls import path

from hub.views import (
    index,
    PositionsListView,
    WorkersListView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "positions/",
        PositionsListView.as_view(),
        name="position-list",
    ),
    path(
        "workers/",
        WorkersListView.as_view(),
        name="worker-list",
    ),
]

app_name = "hub"