from django.contrib import admin
from . models import Profile,Speaker,Schedule,Comment


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'position')
    


admin.site.register(Profile)
admin.site.register(Speaker,SpeakerAdmin)
admin.site.register(Schedule)
admin.site.register(Comment)