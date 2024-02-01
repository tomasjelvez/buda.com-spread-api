import requests


class BudaApi:
    base_url = "https://www.buda.com/api/v2"

    def get_markets(self) -> dict:
        return requests.get(f"{self.base_url}/markets").json()

    def get_market(self, mid: str):
        return requests.get(f"{self.base_url}/markets/{mid}").json()

    def get_market_trades(self, mid: str):
        return requests.get(f"{self.base_url}/markets/{mid}/trades").json()

    def get_market_spread(self, mid: str):
        try:
            market_trades = self.get_market_trades(mid)["trades"]["entries"]
            max_buy_price = 0
            min_sell_price = float("inf")
            for trade in market_trades:
                trade_type = trade[3]
                trade_price = float(trade[2])
                if trade_type == "sell" and trade_price < min_sell_price:
                    min_sell_price = trade_price
                if trade_type == "buy" and trade_price > max_buy_price:
                    max_buy_price = trade_price
            # ensure to find a buy and sell price, else return 0
            if min_sell_price == float("inf") or max_buy_price == 0:
                return 0
            return max_buy_price - min_sell_price

        except:
            return -1

    def get_all_markets_spread(self):
        # Handle Buda API Errors or Downtimes
        try:
            markets = self.get_markets()["markets"]
            markets_spread = {}
            for market in markets:
                mid = market["id"]
                spread = self.get_market_spread(mid)
                markets_spread[mid] = spread
            return markets_spread
        except:
            return -1
