from django.contrib import admin
from .models import *

# Register your models here.
class TesterAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tester._meta.fields]
class ChildAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Child._meta.fields]

admin.site.register(Tester, TesterAdmin)
admin.site.register(Child, ChildAdmin)