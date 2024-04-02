from django.contrib import admin

# Register your models here.

from .models import Posts, Author, tag

class PostAdmin(admin.ModelAdmin): 
    prepopulated_fields = {"slug" : ("title",)}
    list_filter = ("date", "author",)
    list_display = ("title", "author",)



admin.site.register(Posts, PostAdmin)
admin.site.register(Author)
admin.site.register(tag)