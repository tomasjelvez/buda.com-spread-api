from django.test import TestCase
import requests
from rest_framework.test import APITestCase
from unittest.mock import call, mock_open, patch
from rest_framework.request import Request
from django.http import HttpRequest
from spreadApi.BudaApiConsumer.markets import BudaApi
from spreadApi.views import (
    AlertSpreadPollingApi,
    BudaMarketSpreadApi,
    BudaMarketSpreadDetailApi,
)


class SpreadApiViewsTests(APITestCase):
    def setUp(self):
        self.buda_client = BudaApi()

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_all_markets_spread")
    def test_get_all_markets_spread_view_ok(self, mock_get_all_markets_spread):
        mock_get_all_markets_spread.return_value = {
            "BTC-CLP": 412102.0,
            "BTC-COP": 4364594.99000001,
        }
        response = BudaMarketSpreadApi.get(self, None)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_get_all_markets_spread.call_count, 1)

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_all_markets_spread")
    def test_get_all_markets_spread_view_error(self, mock_get_all_markets_spread):
        mock_get_all_markets_spread.return_value = -1
        response = BudaMarketSpreadApi.get(self, None)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(mock_get_all_markets_spread.call_count, 1)

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    def test_get_market_spread_view_ok(self, mock_get_market_spread):
        mock_get_market_spread.return_value = 412102.0
        response = BudaMarketSpreadDetailApi.get(self, None, "BTC-CLP")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_get_market_spread.call_count, 1)

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    def test_get_market_spread_view_error(self, mock_get_market_spread):
        mock_get_market_spread.return_value = -1
        response = BudaMarketSpreadDetailApi.get(self, None, "BTC-CLP")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(mock_get_market_spread.call_count, 1)

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_get_alert_spread_polling_view_create(
        self, mock_open_file, mock_get_market_spread
    ):
        mock_get_market_spread.return_value = 412102.0
        response = AlertSpreadPollingApi.get(self, Request(HttpRequest()), "BTC-BRL")
        self.assertEqual(
            response.data,
            {"market_id": "BTC-BRL", "spread": 412102.0, "status": "created"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_get_market_spread.call_count, 1)
        mock_open_file.call_args_list == [call("BTC-BRL_alert_spread.json", "r+")]

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    @patch("builtins.open", new_callable=mock_open, read_data="1")
    def test_get_alert_spread_polling_view_updated(
        self, mock_open_file, mock_get_market_spread
    ):
        mock_get_market_spread.return_value = 412102.0
        response = AlertSpreadPollingApi.get(self, Request(HttpRequest()), "BTC-CLP")
        self.assertEqual(
            response.data,
            {"market_id": "BTC-CLP", "spread": 412102.0, "status": "updated"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_get_market_spread.call_count, 1)
        mock_open_file.assert_called_once_with("BTC-CLP_alert_spread.json", "r+")

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    @patch("builtins.open", new_callable=mock_open, read_data="412102.0")
    def test_get_alert_spread_polling_view_not_updated(
        self, mock_open_file, mock_get_market_spread
    ):
        mock_get_market_spread.return_value = 412102.0
        response = AlertSpreadPollingApi.get(self, Request(HttpRequest()), "BTC-CLP")
        self.assertEqual(
            response.data,
            {"market_id": "BTC-CLP", "spread": 412102.0, "status": "not updated"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_get_market_spread.call_count, 1)
        mock_open_file.assert_called_once_with("BTC-CLP_alert_spread.json", "r+")
