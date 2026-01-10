from django.urls import path

from hub.views import (
    index,
    PositionsListView,
    PositionsCreateView,
    PositionUpdateView,
    PositionDeleteView,
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
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
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