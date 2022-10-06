from django.contrib import admin
from todolist.models import Tasks
from todolist.models import Type
from todolist.models import Status


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'type', 'status', 'created_at', 'updated_at')
    list_filter = ('id', 'summary', 'description', 'type', 'status', 'created_at', 'updated_at')
    search_fields = ('summary', 'description', 'type', 'status')
    fields = ('summary', 'description', 'type', 'status', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Tasks, TasksAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
    fields = ('name', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Status, StatusAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
    fields = ('name', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Type, TypeAdmin)