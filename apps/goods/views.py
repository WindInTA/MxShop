from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters

# from .filters import GoodsFilter
from .filters import GoodsFilter
from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory


# class GoodsListView(APIView):
#     """
#     List all goods.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self,request,format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
# return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # 因为ListAPIView 里面直接继承了这两个类，所以看需求直接写
    # ＆ 这个 get函数也不用重写了
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    # authentication_classes = (TokenAuthentication, )
    # 分页

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')

    filter_class = GoodsFilter   # 字段匹配

    search_fields = ('name', 'goods_brief', 'goods_desc')

    ordering_fields = ('sold_num', 'shop_price')
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min",0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #     return queryset
    # # 这个参数比较多，要重复写多变


class CategoryViewset(mixins.ListModelMixin,  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

