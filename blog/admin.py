from django.contrib import admin

# Register your models here.
from .models import Navigation,Context,Comment

class NavigationAdmin(admin.ModelAdmin):
    #fields = ['create_time','nav_name']
    list_display = ('nav_name',)
admin.site.register(Navigation,NavigationAdmin)
#admin.site.register(Navigation)


class ContextAdmin(admin.ModelAdmin):
    list_display = ('title','classify','shortcontext','create_time','hits','times','goods','bads',)

admin.site.register(Context,ContextAdmin)
#admin.site.register(Context)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','content','createtime','name','email',)
admin.site.register(Comment,CommentAdmin)