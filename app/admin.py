from django.contrib import admin
from .models import FamilyMember, Store, ImportantDate, CustomUser



admin.site.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'first_name', 'last_name', 'mobile_phone')
    list_filter = ('id_number','create_at','mobile_phone')
    search_fields = ['id_number']
    date_hierarchy = 'create_at'
    raw_id_field = ('id_number',)


admin.site.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'square_meter', 'province', 'city')
    list_filter = ('user','province','city','square_meter')
    search_fields = ['user']


admin.site.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'relation')
    list_filter = ('user','first_name','last_name','relation')
    search_fields = ['user']


admin.site.register(ImportantDate)
class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ('user', 'occasion', 'date', 'family_member')
    list_filter = ('user','occasion','date','family_member')
    search_fields = ['user']