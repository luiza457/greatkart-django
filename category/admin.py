from django.contrib import admin
from .models import Category 

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # automatically populate slug field 
    prepopulated_fields = {'slug':('category_name',)}

    # displayed fields in the admin's list view
    list_display = ('category_name','slug')

admin.site.register(Category,CategoryAdmin)
