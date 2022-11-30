from django.contrib import admin
from Confession.models import myconfessionmodel, feedbackmodel


class myconfessionmodeladmin(admin.ModelAdmin):
    list_display = ('tosendto', 'facultyis',
                    'confessionmsg', 'youridentification')


class feedbackmodeladmin(admin.ModelAdmin):
    list_display = ('feedbackdetails', 'feedbackprovider')


admin.site.register(myconfessionmodel, myconfessionmodeladmin)
admin.site.register(feedbackmodel, feedbackmodeladmin)
