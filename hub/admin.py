from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from hub.models import (
    Worker,
    TaskType,
    Task,
    Position,
)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "priority", "deadline", "is_completed",)

admin.site.register(TaskType)
admin.site.register(Position)
