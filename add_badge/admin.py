from django.contrib import admin
from .models import Badge, BadgeRequirements
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
admin.site.register(BadgeRequirements) 


@admin.register(Badge)
class Badgeadmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'description', 'category')
    search_fields = ['name', 'content']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content',)
