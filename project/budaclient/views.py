from rest_framework.response import Response
from rest_framework.views import APIView

from budaclient.BudaApiConsumer.markets import BudaApi

# Create your views here.


class BudaMarketSpreadApi(APIView):
    client = BudaApi()

    def get(self, request, format=None, *args, **kwargs):
        return Response(self.client.get_all_markets_spread())


class BudaMarketSpreadDetailApi(BudaMarketSpreadApi):
    def get(self, request, mid, format=None, *args, **kwargs):
        return Response(
            {"market_id": mid, "spread": self.client.get_market_spread(mid)}
        )
