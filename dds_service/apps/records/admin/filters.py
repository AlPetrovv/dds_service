from typing import Type

from django.contrib.admin import SimpleListFilter
from django.db.models import Model


def simple_filter(
        rel_model: Type[Model],
        title: str,
        parameter_name: str,
        display_field: str,
        lookup_name: str|None = None
):
    """
    Base filter function that prepares the filter for the model.
    :param rel_model: Django model
    :param title: text that will be displayed as a title
    :param parameter_name: parameter for lookup
    :param display_field: field that will be displayed as a value
    :param lookup_name: if it is not None, it will be used as a lookup, otherwise it will be used as a parameter
    :return: BaseFilter
    """
    class BaseFilter(SimpleListFilter):
        def __init__(self, request, params, model, model_admin):
            self.parameter_name = parameter_name
            self.title = title
            super().__init__(request, params, model, model_admin)


        def lookups(self, request, model_admin):
            models = rel_model.objects.filter()
            return [(m.id, getattr(m, display_field)) for m in models] # noqa

        def queryset(self, request, queryset):
            value_id = self.value()
            if value_id is None:
                return queryset
            return queryset.filter(**{f"{lookup_name or parameter_name}__id": value_id})

    return BaseFilter