from django.contrib import admin

from apps.categories.models import Category, SubCategory


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0
    max_num = 5
    fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (SubCategoryInline,)
    required_fields = ("record_type", "name")
    list_display = (
        "name",
        "record_type"
    )
    search_fields = (
        "name",
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
    )
    search_fields = (
        "name",
    )
