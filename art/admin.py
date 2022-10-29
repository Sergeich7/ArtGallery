
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
    list_display = ('title', 'category', 'technique', 'created',)
    list_display_links = ('title',)
#    list_editable = ('created',)
    search_fields = ('title', 'description',)
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fields = (
        ('title', 'created'),
        'description',
        ('category', 'technique',),
        ('materials', 'size',),
        ('author', 'slug',),
    )


@admin.register(a_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(a_models.Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('last_name', 'first_name', 'patronymic',)}


@admin.register(a_models.Technique)
class TechniqueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(a_models.ArtComment)
class ArtCommentAdmin(admin.ModelAdmin):
    list_display = ('published', 'user', 'product', 'text')
    list_display_links = ('published', 'text',)
    search_fields = ('text',)

