from django.contrib import admin
from .models import Post, Category, Comment, Tag, UserProfile


@admin.register(Post)
class PersonAdmin(admin.ModelAdmin):
    date_hierarchy = 'post_date'
    list_display = ("title", "owner")
    list_filter = ("title",)
    search_fields = ['title']
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'description', 'bodytext', 'image', 'owner')
        }),

        ('tag category', {
            'classes': ('collapse',),
            'fields': ('tag', 'category'),
        }),
    )


@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ['name']


@admin.register(Comment)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_filter = ("name",)
    search_fields = ['name']


@admin.register(Tag)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("tag_name",)
    list_filter = ("tag_name",)
    search_fields = ['tag_name']


@admin.register(UserProfile)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("user",)
    search_fields = ['user']
