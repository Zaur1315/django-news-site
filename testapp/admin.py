from .models import Rubric, Article
from mptt.admin import DraggableMPTTAdmin
from django.contrib import admin

admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title'
    ),
    list_display_links=(
        'indented_title',
    ),
)


admin.site.register(Article)
