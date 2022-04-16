from django.contrib import admin

# Register your models here.
from .models import User

class Admin(admin.ModelAdmin):
    list_display = ["username","email","name","last","time"]
    list_filter = ["username","email","name","last","time"]
    list_editable = ["email"]
    search_field = ["username","email","name","last"]
    class Meta:
        model = User

admin.site.register(User,Admin)