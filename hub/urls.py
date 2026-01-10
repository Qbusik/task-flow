from django.urls import path

from hub.views import index, PositionsListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "positions/",
        PositionsListView.as_view(),
        name="position-list",
    ),
]

app_name = "hub"