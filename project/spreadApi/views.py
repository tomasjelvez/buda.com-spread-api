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
            Response({"mid": mid, "spread": spread})
            if spread != -1
            else Response("Error getting market.", status=500)
        )


class AlertSpreadPollingApi(BudaMarketSpreadApi):
    def get(self, request, mid, *args, **kwargs):
        current_spread = self.buda_client.get_market_spread(mid)
        if current_spread == -1:
            return Response(
                {
                    "mid": mid,
                    "error": f"Error getting current spread",
                },
                status=500,
            )  # get the alert spread from a json cache file, if it doesnt exist, return an error message
        try:
            with open(f"{mid}_alert_spread.json", "r+") as file:
                alert_spread = float(file.read())
                if current_spread > alert_spread:
                    return Response(
                        {
                            "mid": mid,
                            "current_spread": current_spread,
                            "alert_spread": alert_spread,
                            "status": "greater",
                        }
                    )
                elif current_spread < alert_spread:
                    return Response(
                        {
                            "mid": mid,
                            "current_spread": current_spread,
                            "alert_spread": alert_spread,
                            "status": "lower",
                        }
                    )
                else:
                    return Response(
                        {
                            "mid": mid,
                            "current_spread": current_spread,
                            "alert_spread": alert_spread,
                            "status": "equal",
                        }
                    )
        except Exception as e:
            return Response(
                {
                    "mid": mid,
                    "error": f"Error getting alert spread",
                },
                status=404,
            )

    def post(self, request, mid, *args, **kwargs):
        try:
            alert_spread = float(request.data.get("alert_spread"))
            with open(f"{mid}_alert_spread.json", "w+") as file:
                file.seek(0)
                file.write(str(alert_spread))
                file.close()
                return Response(
                    {
                        "mid": mid,
                        "alert_spread": alert_spread,
                        "status": "created",
                    }
                )
        except:
            return Response(
                {
                    "mid": mid,
                    "error": f"Error setting alert spread",
                },
                status=500,
            )
