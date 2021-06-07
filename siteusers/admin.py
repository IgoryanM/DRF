from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from siteusers.models import SiteUsers

admin.site.register(SiteUsers, UserAdmin)
