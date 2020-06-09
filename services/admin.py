from django.contrib import admin
from services.models import New_Project

# Register your models here.
#La sig clase convencoinalmente se nombra ProjectAdmin
class Admin_Projects(admin.ModelAdmin):
    readonly_fields = ('created','modified')
    
admin.site.register(New_Project,Admin_Projects)

