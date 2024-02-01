from rest_framework.response import Response
from rest_framework.views import APIView

from spreadApi.BudaApiConsumer.markets import BudaApi

# Create your views here.


class BudaMarketSpreadApi(APIView):
    client = BudaApi()

    def get(self, request, format=None, *args, **kwargs):
        response = self.client.get_all_markets_spread()
        return (
            Response(response)
            if response != -1
            else Response("Error getting markets.", status=500)
        )


class BudaMarketSpreadDetailApi(BudaMarketSpreadApi):
    def get(self, request, mid, format=None, *args, **kwargs):
        spread = self.client.get_market_spread(mid)
        return (
            Response({"market_id": mid, "spread": spread})
            if spread != -1
            else Response("Error getting market.", status=500)
        )
