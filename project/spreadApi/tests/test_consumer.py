from rest_framework.test import APITestCase
from unittest.mock import call, patch

from spreadApi.BudaApiConsumer.markets import BudaApi


class BudaApiConsumerTests(APITestCase):
    def setUp(self):
        self.buda_client = BudaApi()

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_trades")
    def test_get_market_spread(self, mock_get_market_trades):
        mock_get_market_trades.return_value = {
            "trades": {
                "mid": "BTC-CLP",
                "timestamp": None,
                "last_timestamp": "1706734965124",
                "entries": [
                    ["1706740026301", "0.00246504", "40078752.0", "buy", 7826847],
                    ["1706739914594", "0.02463685", "40102036.0", "buy", 7826846],
                    ["1706739839523", "0.00744935", "39900000.0", "sell", 7826845],
                    ["1706739839523", "0.00025065", "39900001.0", "sell", 7826844],
                    ["1706739802976", "0.00061884", "39913284.97", "buy", 7826843],
                    ["1706739661670", "0.00691422", "39920506.0", "buy", 7826842],
                    ["1706739661670", "0.00051893", "39918531.0", "buy", 7826841],
                    ["1706739500425", "0.00007426", "39910046.99", "buy", 7826840],
                    ["1706738759419", "0.0048834", "39375251.0", "sell", 7826839],
                    ["1706738552986", "0.00496444", "39801933.0", "buy", 7826838],
                    ["1706738426398", "0.00177378", "39370996.0", "sell", 7826837],
                    ["1706738426398", "0.00130289", "39370996.01", "sell", 7826836],
                    ["1706738280249", "0.00124041", "39824797.0", "buy", 7826835],
                    ["1706738058295", "0.0127083", "39344355.0", "sell", 7826834],
                    ["1706738002316", "0.00146075", "39318472.01", "sell", 7826833],
                    ["1706738002316", "0.00031937", "39344352.81", "sell", 7826832],
                    ["1706737850071", "0.00037124", "39865433.0", "buy", 7826831],
                    ["1706737313864", "0.00053609", "39789379.0", "sell", 7826830],
                    ["1706737313291", "0.019", "39789379.0", "sell", 7826829],
                    ["1706737311985", "0.00276364", "39789369.99", "buy", 7826828],
                    ["1706737311985", "0.00031937", "39789369.99", "buy", 7826827],
                    ["1706737275375", "0.06174988", "39318500.0", "sell", 7826826],
                    ["1706737253190", "0.0471958", "39318500.0", "sell", 7826825],
                    ["1706737253190", "0.00002541", "39333333.0", "sell", 7826824],
                    ["1706737253190", "0.00400249", "39333333.0", "sell", 7826823],
                    ["1706737179138", "0.01241281", "39797111.0", "buy", 7826822],
                    ["1706737159057", "0.00362462", "39333333.0", "sell", 7826821],
                    ["1706737159057", "0.00000421", "39480449.0", "sell", 7826820],
                    ["1706737103308", "0.00620555", "39802627.0", "buy", 7826819],
                    ["1706737027735", "0.01489047", "39809298.0", "buy", 7826818],
                    ["1706736916662", "0.01612833", "39817412.0", "buy", 7826817],
                    ["1706736609346", "0.00024908", "39480449.0", "sell", 7826816],
                    ["1706736609346", "0.00037994", "39480454.0", "sell", 7826815],
                    ["1706736609346", "0.05764509", "39500000.0", "sell", 7826814],
                    ["1706736609346", "0.00052589", "39590002.0", "sell", 7826813],
                    ["1706736563252", "0.00022316", "39844320.0", "buy", 7826812],
                    ["1706736445137", "0.002", "39590002.0", "sell", 7826811],
                    ["1706736401909", "0.00266548", "39744215.0", "buy", 7826810],
                    ["1706736355840", "0.09715284", "39500000.0", "sell", 7826809],
                    ["1706736355840", "0.21714716", "39500021.0", "sell", 7826808],
                    ["1706736351369", "0.02226284", "39500021.0", "sell", 7826807],
                    ["1706736351369", "0.00002525", "39590000.0", "sell", 7826806],
                    ["1706736351369", "0.00002357", "39590000.0", "sell", 7826805],
                    ["1706736291209", "0.0063", "39590000.0", "sell", 7826804],
                    ["1706735994137", "0.02474949", "39913951.0", "buy", 7826803],
                    ["1706735651614", "0.00123932", "39921377.0", "buy", 7826802],
                    ["1706734986249", "0.00049541", "39885072.0", "buy", 7826801],
                    ["1706734965124", "0.00014259", "39502012.0", "sell", 7826800],
                    ["1706734965124", "0.00005063", "39502013.0", "sell", 7826799],
                    ["1706734965124", "0.00005964", "39694002.0", "sell", 7826798],
                ],
            }
        }
        response = self.buda_client.get_market_spread("BTC-CLP")
        self.assertEqual(response, 783563.9900000021)
        mock_get_market_trades.assert_called_once_with("BTC-CLP")

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_markets")
    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    def test_get_all_markets_spread(self, mock_get_market_spread, mock_get_markets):
        mock_get_markets.return_value = {
            "markets": [
                {
                    "id": "BTC-CLP",
                    "name": "btc-clp",
                    "base_currency": "BTC",
                    "quote_currency": "CLP",
                    "minimum_order_amount": ["0.00002", "BTC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "BTC-COP",
                    "name": "btc-cop",
                    "base_currency": "BTC",
                    "quote_currency": "COP",
                    "minimum_order_amount": ["0.00002", "BTC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "ETH-CLP",
                    "name": "eth-clp",
                    "base_currency": "ETH",
                    "quote_currency": "CLP",
                    "minimum_order_amount": ["0.001", "ETH"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "ETH-BTC",
                    "name": "eth-btc",
                    "base_currency": "ETH",
                    "quote_currency": "BTC",
                    "minimum_order_amount": ["0.001", "ETH"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "BTC-PEN",
                    "name": "btc-pen",
                    "base_currency": "BTC",
                    "quote_currency": "PEN",
                    "minimum_order_amount": ["0.00002", "BTC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "ETH-PEN",
                    "name": "eth-pen",
                    "base_currency": "ETH",
                    "quote_currency": "PEN",
                    "minimum_order_amount": ["0.001", "ETH"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "ETH-COP",
                    "name": "eth-cop",
                    "base_currency": "ETH",
                    "quote_currency": "COP",
                    "minimum_order_amount": ["0.001", "ETH"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "BCH-BTC",
                    "name": "bch-btc",
                    "base_currency": "BCH",
                    "quote_currency": "BTC",
                    "minimum_order_amount": ["0.001", "BCH"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "BCH-CLP",
                    "name": "bch-clp",
                    "base_currency": "BCH",
                    "quote_currency": "CLP",
                    "minimum_order_amount": ["0.001", "BCH"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "BCH-COP",
                    "name": "bch-cop",
                    "base_currency": "BCH",
                    "quote_currency": "COP",
                    "minimum_order_amount": ["0.001", "BCH"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "BCH-PEN",
                    "name": "bch-pen",
                    "base_currency": "BCH",
                    "quote_currency": "PEN",
                    "minimum_order_amount": ["0.001", "BCH"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "BTC-ARS",
                    "name": "btc-ars",
                    "base_currency": "BTC",
                    "quote_currency": "ARS",
                    "minimum_order_amount": ["0.00002", "BTC"],
                    "disabled": True,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "50.0",
                },
                {
                    "id": "ETH-ARS",
                    "name": "eth-ars",
                    "base_currency": "ETH",
                    "quote_currency": "ARS",
                    "minimum_order_amount": ["0.001", "ETH"],
                    "disabled": True,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "50.0",
                },
                {
                    "id": "BCH-ARS",
                    "name": "bch-ars",
                    "base_currency": "BCH",
                    "quote_currency": "ARS",
                    "minimum_order_amount": ["0.001", "BCH"],
                    "disabled": True,
                    "illiquid": False,
                    "rpo_disabled": True,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "50.0",
                },
                {
                    "id": "LTC-BTC",
                    "name": "ltc-btc",
                    "base_currency": "LTC",
                    "quote_currency": "BTC",
                    "minimum_order_amount": ["0.003", "LTC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "LTC-CLP",
                    "name": "ltc-clp",
                    "base_currency": "LTC",
                    "quote_currency": "CLP",
                    "minimum_order_amount": ["0.003", "LTC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "LTC-COP",
                    "name": "ltc-cop",
                    "base_currency": "LTC",
                    "quote_currency": "COP",
                    "minimum_order_amount": ["0.003", "LTC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "LTC-PEN",
                    "name": "ltc-pen",
                    "base_currency": "LTC",
                    "quote_currency": "PEN",
                    "minimum_order_amount": ["0.003", "LTC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": None,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "0.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "LTC-ARS",
                    "name": "ltc-ars",
                    "base_currency": "LTC",
                    "quote_currency": "ARS",
                    "minimum_order_amount": ["0.003", "LTC"],
                    "disabled": True,
                    "illiquid": False,
                    "rpo_disabled": True,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "50.0",
                },
                {
                    "id": "USDC-CLP",
                    "name": "usdc-clp",
                    "base_currency": "USDC",
                    "quote_currency": "CLP",
                    "minimum_order_amount": ["0.01", "USDC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "25.0",
                    "taker_discount_percentage": "25.0",
                },
                {
                    "id": "USDC-COP",
                    "name": "usdc-cop",
                    "base_currency": "USDC",
                    "quote_currency": "COP",
                    "minimum_order_amount": ["0.01", "USDC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "50.0",
                    "taker_discount_percentage": "50.0",
                },
                {
                    "id": "USDC-PEN",
                    "name": "usdc-pen",
                    "base_currency": "USDC",
                    "quote_currency": "PEN",
                    "minimum_order_amount": ["0.01", "USDC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "50.0",
                    "taker_discount_percentage": "50.0",
                },
                {
                    "id": "USDC-ARS",
                    "name": "usdc-ars",
                    "base_currency": "USDC",
                    "quote_currency": "ARS",
                    "minimum_order_amount": ["0.01", "USDC"],
                    "disabled": True,
                    "illiquid": False,
                    "rpo_disabled": False,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "50.0",
                },
                {
                    "id": "BTC-USDC",
                    "name": "btc-usdc",
                    "base_currency": "BTC",
                    "quote_currency": "USDC",
                    "minimum_order_amount": ["0.00002", "BTC"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": True,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "0.0",
                },
                {
                    "id": "USDT-USDC",
                    "name": "usdt-usdc",
                    "base_currency": "USDT",
                    "quote_currency": "USDC",
                    "minimum_order_amount": ["0.01", "USDT"],
                    "disabled": False,
                    "illiquid": False,
                    "rpo_disabled": True,
                    "taker_fee": 0.8,
                    "maker_fee": 0.4,
                    "max_orders_per_minute": 100,
                    "maker_discount_percentage": "100.0",
                    "taker_discount_percentage": "100.0",
                },
            ]
        }
        self.buda_client.get_all_markets_spread()
        self.assertEqual(
            mock_get_market_spread.call_args_list,
            [call(market["id"]) for market in mock_get_markets.return_value["markets"]],
        )
