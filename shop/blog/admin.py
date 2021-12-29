from django.contrib import admin
from .models import Post,Category,Comment,Tag, UserProfile
from .forms import PostForm
from django.utils.html import format_html

@admin.register(Post)
class PersonAdmin(admin.ModelAdmin):
    date_hierarchy = 'post_date'
    list_display = ("title", "owner")
    
    fieldsets = (
        (None, {
            'fields': (('title', 'description'),'bodytext' , 'image', 'owner')
        }),

        ('maktab sharif', {
            'classes': ('collapse',),
            'fields': ('tag','category'),
        }),
    )
    
@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Tag)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(UserProfile)
class PersonAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Comment)
# admin.site.register(Tag)

# admin.site.register(UserProfile)