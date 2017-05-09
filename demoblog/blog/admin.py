from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    """ 
    A ModelAdmin class for Post model
    Adds a horizontal filter widget for related tags
    """
    filter_horizontal = ('tags', )


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)