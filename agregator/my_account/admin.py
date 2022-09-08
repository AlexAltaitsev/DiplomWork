from django.contrib import admin

from .models import User, Post

# Register your models here.


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    pass

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    pass