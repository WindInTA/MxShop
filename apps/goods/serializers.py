from rest_framework import serializers

from goods.models import Goods, GoodsCategory


# 一个就是Serializer
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0,)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         return a good instance
#         :param validated_data:
#         :return:
#         """
#
#         return Goods.objects.create(**validated_data)

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)    # 匹配可能会有很多个，所以要写many=true

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 一个是ModelSerializer
class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time',)
        fields = "__all__"   # 显示所有的


class GoodCategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"
