from django.contrib import admin
from MyPetstagramProject.common.models import PhotoComment


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass
