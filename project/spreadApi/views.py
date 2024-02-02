from rest_framework.response import Response
from rest_framework.views import APIView

from spreadApi.BudaApiConsumer.markets import BudaApi

# Create your views here.


class BudaMarketSpreadApi(APIView):
    buda_client = BudaApi()

    def get(self, request, format=None, *args, **kwargs):
        response = self.buda_client.get_all_markets_spread()
        return (
            Response(response)
            if response != -1
            else Response("Error getting markets.", status=500)
        )


class BudaMarketSpreadDetailApi(BudaMarketSpreadApi):
    def get(self, request, mid, format=None, *args, **kwargs):
        spread = self.buda_client.get_market_spread(mid)
        return (
            Response({"market_id": mid, "spread": spread})
            if spread != -1
            else Response("Error getting market.", status=500)
        )


class AlertSpreadPollingApi(BudaMarketSpreadApi):
    def get(self, request, mid, *args, **kwargs):
        current_spread = (
            float(request.query_params.get("spread"))
            if request.query_params
            else self.buda_client.get_market_spread(mid)
        )
        # get the alert spread from a json cache file, if it doesnt exist, we create it
        try:
            with open(f"{mid}_alert_spread.json", "r+") as file:
                alert_spread = float(file.read())
                if current_spread != alert_spread:
                    # overwrite file with new spread
                    file.seek(0)
                    file.write(str(current_spread))
                    file.close()
                    return Response(
                        {
                            "market_id": mid,
                            "spread": current_spread,
                            "status": "updated",
                        }
                    )
                else:
                    return Response(
                        {
                            "market_id": mid,
                            "spread": current_spread,
                            "status": "not updated",
                        }
                    )
        except Exception as e:
            with open(f"{mid}_alert_spread.json", "w+") as file:
                file.seek(0)
                file.write(str(current_spread))
                file.close()
            return Response(
                {"market_id": mid, "spread": current_spread, "status": "created"}
            )
