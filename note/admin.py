from django.contrib import admin
from note.models import UserProfile, Note, Rating

# class NoteAdmin(admin.ModelAdmin):
    # list_display = ('title','note_id','subject', 'module', 'date', 'format')

# class RatingAdmin(admin.ModelAdmin):
    # list_display = ('note','stars')

# class UserProfileAdmin(admin.ModelAdmin):
    # list_display = ('email','name','surname')


# admin.site.register(Rating, RatingAdmin)
# admin.site.register(Note, NoteAdmin)
# admin.site.register(UserProfile)
admin.site.register(Note)
admin.site.register(Rating)