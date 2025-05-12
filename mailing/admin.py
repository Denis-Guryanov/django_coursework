from django.contrib import admin

from .models import Mailing, MailingAttempt, Message, Recipient

admin.site.register(Recipient)
admin.site.register(Message)
admin.site.register(MailingAttempt)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "message", "owner")
    search_fields = ("title", "content")
