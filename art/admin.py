
from django.contrib import admin

import art.models as a_models

admin.site.site_header = 'Арт-галерея'
admin.site.site_title = 'Арт-галерея'

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = a_models.Gallery


class VideoInline(admin.TabularInline):
    fk_name = 'product'
    model = a_models.Video


@admin.register(a_models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, VideoInline]
    list_display = ('title', 'category', 'technique')
    list_display_links = ('title',)
    search_fields = ('title', 'description',)
    ordering = ('title',)


@admin.register(a_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(a_models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(a_models.Technique)
class TechniqueAdmin(admin.ModelAdmin):
    pass


@admin.register(a_models.ArtComment)
class ArtCommentAdmin(admin.ModelAdmin):
    list_display = ('published', 'user', 'product', 'text')
    list_display_links = ('published', 'text',)
    search_fields = ('text',)

