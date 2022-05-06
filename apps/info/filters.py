import django_filters
from django.contrib import admin
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.info.models import Partner


class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class YearFestivalFilterSet(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name="festival__year")


class PartnerFilterSet(django_filters.FilterSet):
    types = CharInFilter(field_name="type", lookup_expr="in")

    class Meta:
        model = Partner
        fields = (
            "types",
            "in_footer_partner",
        )


class HasReviewAdminFilter(admin.SimpleListFilter):
    title = _("Есть отзыв?")
    parameter_name = "volunteer"

    def lookups(self, request, model_admin):
        return (
            ("True", _("Да")),
            ("False", _("Нет")),
        )

    def queryset(self, request, queryset):
        if self.value() == "True":
            return queryset.filter(~Q(review_text__exact=""))
        if self.value() == "False":
            return queryset.filter(review_text__exact="")


class PartnerTypeFilter(admin.SimpleListFilter):
    title = _("Тип партнера")
    parameter_name = "type"

    def lookups(self, request, model_admin):
        partner_types_list = [
            (None, _("Генеральный партнер")),  # default lookup which is used instead of 'All' ('Все')
            ("festival", _("Партнер фестиваля")),
            ("info", _("Информационный партнер")),
        ]
        return partner_types_list

    def queryset(self, request, queryset):
        if self.value() is None:  # get qs for new default lookup
            return Partner.objects.filter(type="general")
        if self.value() == "festival":
            return Partner.objects.filter(type="festival")
        if self.value() == "info":
            return Partner.objects.filter(type="info")

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                "selected": self.value() == lookup,
                "query_string": changelist.get_query_string(
                    {
                        self.parameter_name: lookup,
                    },
                    [],
                ),
                "display": title,
            }
