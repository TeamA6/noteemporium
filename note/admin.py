from django.contrib import admin
from note.models import Note, Rating, UserProfile, Module, Subject

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','note_id','subject', 'module', 'date', 'format')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('note','stars')

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('sub','moduleTitle','abb')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subjectTitle',)


admin.site.register(Rating, RatingAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(UserProfile)

# admin.site.register(Note)
# admin.site.register(Rating)
