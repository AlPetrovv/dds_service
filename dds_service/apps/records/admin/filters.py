from typing import Type

from django.contrib.admin import SimpleListFilter, FieldListFilter
from django.db.models import Model

from apps.categories.models import Category, SubCategory
from apps.records.models import RecordStatus, RecordType


def simple_filter(model: Type[Model], title: str,  parameter_name: str):
    class BaseFilter(SimpleListFilter):
        nonlocal model, title, parameter_name
        title = title
        parameter_name = parameter_name

        def lookups(self, request, model_admin):
            models = model.objects.filter()
            return [(m.id, m.name) for m in models]  # noqa

        def queryset(self, request, queryset):
            value_id = self.value()
            if value_id is None:
                return queryset
            return queryset.filter(**{f"{parameter_name}__id": value_id})

    return BaseFilter


class CategoryFilter(SimpleListFilter):
    title = "Category"
    parameter_name = "category__name"

    def lookups(self, request, model_admin):
        categories = Category.objects.filter()
        return [(c.id, c.name) for c in categories]

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id is None:
            return queryset
        return queryset.filter(category_id=category_id)


class SubCategoryFilter(SimpleListFilter):
    title = "SubCategory"
    parameter_name = "category__subcategories__name"

    def lookups(self, request, model_admin):
        subcategories = SubCategory.objects.filter()
        return [(sc.id, sc.name) for sc in subcategories]

    def queryset(self, request, queryset):
        subcategory_id = self.value()
        if subcategory_id is None:
            return queryset
        qs = queryset.filter(category__subcategories__id=subcategory_id)
        return qs


class RecordStatusFilter(SimpleListFilter):
    title = "Status"
    parameter_name = "status__name"

    def lookups(self, request, model_admin):
        statuses = RecordStatus.objects.filter()
        return [(s.id, s.name) for s in statuses]

    def queryset(self, request, queryset):
        status_id = self.value()
        if status_id is None:
            return queryset
        return queryset.filter(status_id=status_id)


class RecordTypeFilter(SimpleListFilter):
    title = "Type"
    parameter_name = "type__name"

    def lookups(self, request, model_admin):
        types = RecordType.objects.filter()
        return [(t.id, t.name) for t in types]

    def queryset(self, request, queryset):
        type_id = self.value()
        if type_id is None:
            return queryset
        return queryset.filter(type_id=type_id)
