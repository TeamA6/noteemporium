from django.contrib import admin
from note.models import Note, Rating, UserProfile

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','note_id','subject', 'module', 'date', 'format')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('note','stars')


admin.site.register(Rating, RatingAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(UserProfile)

# admin.site.register(Note)
# admin.site.register(Rating)