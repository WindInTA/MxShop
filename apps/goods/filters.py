from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Goods


class GoodsFilter(filters.FilterSet):
    price_min = filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = filters.NumberFilter(name='shop_price', lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
