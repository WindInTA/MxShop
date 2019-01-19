import json

from django.core import serializers
from django.http import JsonResponse
from django.views.generic.base import View
from django.forms.models import model_to_dict


from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的View实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     # 仅仅是为了演示，就写一小段
        #     json_dict = dict()
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_dict["add_time"] = good.add_time
        #     json_list.append(json_dict)

        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)
        # 但是有些格式还是不能序列化，例如ImageFieldFies

        json_data = serializers.serialize("json",goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse
        # return HttpResponse(json.dumps(json_data), content_type="application/json")
        return JsonResponse(json_data,safe=False )