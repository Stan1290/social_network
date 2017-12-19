from django.contrib import admin
from groups import models


class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
