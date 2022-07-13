
import django_filters
from .models import *
from django_filters import DateFilter,CharFilter,RangeFilter
class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name",lookup_expr='icontains')
    price = CharFilter(field_name="price",lookup_expr='icontains')
    # start_date= DateFilter(field_name="release_date",lookup_expr='gte')
    # end_date= DateFilter(field_name="release_date",lookup_expr='lte')
    # start_price= CharFilter(field_name="price",lookup_expr='gte')
    # end_price= CharFilter(field_name="price",lookup_expr='lte')
    # price= RangeFilter(field_name="price",lookup_expr='icontains')


    class Meta:
        model = Product
        fields = ['price', 'release_date']
        exclude = ['Product','release_date']