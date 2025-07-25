from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from apps.categories.models import Category
from apps.records.admin.filters import SubCategoryFilter, CategoryFilter, simple_filter
from apps.records.models import Record, RecordStatus, RecordType


@admin.register(RecordStatus)
class RecordStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(RecordType)
class RecordTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "amount",
        "status",
        "type",
        "category",
        "subcategories",
        "comment",
    )
    ordering = ("-created_at",)
    list_filter = (
        ("created_at", DateRangeFilter),
        simple_filter(Category, "Category", "category"),
        SubCategoryFilter
    )

    @admin.display(description="Subcategories")
    def subcategories(self, obj):
        return ", ".join([sc.name for sc in obj.category.subcategories.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("category", "category__subcategories")
