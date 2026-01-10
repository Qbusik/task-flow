from django.urls import path

from hub.views import (
    index,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskTypeListView,
    TaskListView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
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
        WorkerListView.as_view(),
        name="worker-list",
    ),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail",
    ),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
    path(
        "tasktypes/",
        TaskTypeListView.as_view(),
        name="task_type-list",
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
]

app_name = "hub"