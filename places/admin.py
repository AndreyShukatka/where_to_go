from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin, SortableAdminMixin


class ImageInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = [
        'get_preview'
    ]
    fields = ('image', 'get_preview', 'position')

    def get_preview(self, instance: Image):
        image = instance.image
        return format_html('<img src="{url}" height=200px/>', url=image.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInLine
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin, SortableAdminMixin):
    list_display = ['place']