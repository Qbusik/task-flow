from django.urls import path

from hub.views import (
    index,
    PositionsListView,
    PositionsCreateView,
    WorkersListView,
    TaskTypesListView,
    TasksListView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "positions/",
        PositionsListView.as_view(),
        name="position-list",
    ),
path(
        "positions/create/",
        PositionsCreateView.as_view(),
        name="position-create",
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
    path(
        "tasks/",
        TasksListView.as_view(),
        name="task-list",
    ),
]

app_name = "hub"