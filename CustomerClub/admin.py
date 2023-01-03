from django.contrib import admin
from .models import Gift , Profile, Log

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'score')
    list_filter = ('title','create_at')
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'create_at'
    raw_id_field = ('title',)

admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    raw_id_field = ('customer',)
    list_display = ('customer', 'score_user', 'is_gold')
    list_filter = ('customer','score_user')
    search_fields = ['customer']

        
admin.site.register(Log)
class LogAdmin(admin.ModelAdmin):

    list_display = ('user', 'gift', 'created_at')
    list_filter = ('user','gift')
    search_fields = ['user']

