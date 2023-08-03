from django.contrib import admin
from .models import user,noted
# Register your models here.

class getuser(admin.ModelAdmin):
    ordering = ['id']
    # image_tag.allow_tags = True
    list_display = ['id','fname','lname','uname','city','state','password','created_at','updated_at']
    
admin.site.register(user,getuser)

class getnotes(admin.ModelAdmin):
    readonly_fields = ['file']
    list_display = ['id','query','option','file','comment','created_at','updated_at']

admin.site.register(noted,getnotes)