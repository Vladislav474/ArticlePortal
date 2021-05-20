from django.contrib import admin
from portalapp.models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
     fieldsets = [
        (None,               {'fields': ['slug']}),
        ('Date information', {'fields': ['name']}),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article)
