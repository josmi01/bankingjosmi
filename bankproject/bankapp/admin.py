from django.contrib import admin
from.models import Branches
# Register your models here.

class BranchesAdmin(admin.ModelAdmin):
    list_display = ['name','slug',]
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Branches,BranchesAdmin)




