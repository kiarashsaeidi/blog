from django.contrib import admin

from .models import posts, Author, tag, comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title", )} 






admin.site.register(posts, PostAdmin)
admin.site.register(Author)
admin.site.register(tag)
admin.site.register(comment)