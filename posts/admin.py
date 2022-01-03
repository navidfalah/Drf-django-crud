from django.contrib import admin
from .models import CustomUser, Report, ReportImages


admin.site.register(ReportImages)
admin.site.register(CustomUser)
admin.site.register(Report)