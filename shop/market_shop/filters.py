from django_filters.rest_framework import FilterSet, NumberFilter
from .models import Product


class ProductListFilter(FilterSet):
    min_price = NumberFilter(field_name="price_per_unit", lookup_expr='gte')
    max_price = NumberFilter(field_name="price_per_unit", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['tag_product', 'max_price', 'min_price']
