from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
