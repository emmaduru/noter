from django.contrib import admin

from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Note, NoteAdmin)