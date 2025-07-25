from rangefilter.filters import DateRangeFilter

from django.contrib import admin

from apps.categories.models import Category, SubCategory
from apps.records.models import Record, RecordStatus, RecordType

from .filters import simple_filter


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
        simple_filter(Category, "Category", "category", 'name'),
        simple_filter(SubCategory, "Subcategory", "subcategories", 'name', "category__subcategories"),
        simple_filter(RecordStatus, "Status", "status", 'name'),
        simple_filter(RecordType, "Type", "type", 'name'),
    )

    @admin.display(description="Subcategories")
    def subcategories(self, obj):
        return ", ".join([sc.name for sc in obj.category.subcategories.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("category").prefetch_related("category__subcategories")