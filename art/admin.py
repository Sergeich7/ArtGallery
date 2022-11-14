from django.utils.safestring import mark_safe
from django.contrib import admin

import art.models as a_models

admin.site.site_header = 'Арт-галерея'
admin.site.site_title = 'Арт-галерея'


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = a_models.Gallery
    extra = 4
    readonly_fields = ('prev_photo',)
    classes = ("collapse",)

    def prev_photo(self, object):
        if object.picture:
            return mark_safe(
                f"<a href='{object.picture.url}' target='_blank'>\
                <img src='{object.picture.url}' height='70'></a>")


    prev_photo.short_description = 'Миниатюра'


class VideoInline(admin.TabularInline):
    fk_name = 'product'
    model = a_models.Video
    classes = ("collapse",)


@admin.register(a_models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, VideoInline]
    list_display = ('title', 'thumb_day', 'author', 'category', 'technique',)
    list_display_links = ('title', 'thumb_day', )
#    list_editable = ('created',)
    search_fields = ('title', 'description',)
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    readonly_fields = ('thumb_day',)
    fields = (
        ('title', 'created', 'author',),
        ('category', 'technique', 'materials',),
        ('size', 'slug',),
        ('description', 'thumb_day',),
    )
#    fieldsets = (
#        (None, {
#            "fields": (("title", "tagline"),)
#        }),
#        (None, {
#            "fields": ("description", "poster")
#        }),
#        (None, {
#            "fields": (("year", "world_premiere", "country"),)
#        }),
#        ("Actors", {
#            "classes": ("collapse",),
#            "fields": (("actors", "directors", "genres", "category"),)
#        }),
#        (None, {
#            "fields": (("budget", "fees_in_usa", "fess_in_world"),)
#        }),
#        ("Options", {
#            "fields": (("url", "draft"),)
#        }),
#    )

    def thumb_day(self, object):
        """Показываем миниатюру дня работы, если уже выбрана"""
        if object.thumb_of_day:
            return mark_safe(f"<img src='{object.thumb_of_day.url}' width=70>")
        return ''

    thumb_day.short_description = 'Тумба дня'


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
