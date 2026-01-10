from django.urls import path

from hub.views import (
    index,
    PositionsListView,
    WorkersListView,
    TaskTypesListView
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
    path(
        "tasktypes/",
        TaskTypesListView.as_view(),
        name="task_type-list",
    ),
]

app_name = "hub"