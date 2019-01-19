from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .serializers import GoodsSerializer
from .models import Goods


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
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GoodsListView(generics.ListAPIView):
    # 因为ListAPIView 里面直接继承了这两个类，所以看需求直接写
    # ＆ 这个 get函数也不用重写了
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # 分页
