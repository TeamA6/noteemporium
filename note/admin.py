
from django.contrib import admin
from note.models import Note, Rating, UserProfile, Module, Subject

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','subject', 'module')#, note_id #'date', 'format') removed for time being

class RatingAdmin(admin.ModelAdmin):
    list_display = ('note','stars')

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('sub','moduleTitle','abb')

class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('subjectTitle',)}


admin.site.register(Rating, RatingAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(UserProfile)