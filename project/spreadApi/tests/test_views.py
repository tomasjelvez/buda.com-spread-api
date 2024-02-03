from django.urls import reverse
from rest_framework.test import APITestCase
from unittest.mock import mock_open, patch
from spreadApi.BudaApiConsumer.markets import BudaApi
from spreadApi.views import (
    AlertSpreadPollingApi,
    BudaMarketSpreadApi,
    BudaMarketSpreadDetailApi,
)
from rest_framework import status


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
    @patch("builtins.open", new_callable=mock_open, read_data="412102.0")
    def test_get_alert_spread_polling_view_greater(self, _, mock_get_market_spread):
        mock_get_market_spread.return_value = 412103.0
        response = AlertSpreadPollingApi.get(self, None, "BTC-CLP")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "mid": "BTC-CLP",
                "current_spread": 412103.0,
                "alert_spread": 412102.0,
                "status": "greater",
            },
        )

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    @patch("builtins.open", new_callable=mock_open, read_data="412102.0")
    def test_get_alert_spread_polling_view_lower(self, _, mock_get_market_spread):
        mock_get_market_spread.return_value = 412101.0
        response = AlertSpreadPollingApi.get(self, None, "BTC-CLP")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "mid": "BTC-CLP",
                "current_spread": 412101.0,
                "alert_spread": 412102.0,
                "status": "lower",
            },
        )

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    @patch("builtins.open", new_callable=mock_open, read_data="412101.0")
    def test_get_alert_spread_polling_view_equal(self, _, mock_get_market_spread):
        mock_get_market_spread.return_value = 412101.0
        response = AlertSpreadPollingApi.get(self, None, "BTC-CLP")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "mid": "BTC-CLP",
                "current_spread": 412101.0,
                "alert_spread": 412101.0,
                "status": "equal",
            },
        )

    @patch("spreadApi.BudaApiConsumer.markets.BudaApi.get_market_spread")
    def test_get_alert_spread_polling_view_error(self, mock_get_market_spread):
        mock_get_market_spread.return_value = -1
        response = AlertSpreadPollingApi.get(self, None, "BTC-CLP")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            response.data,
            {
                "mid": "BTC-CLP",
                "error": "Error getting current spread",
            },
        )

    # test post view

    @patch("builtins.open", new_callable=mock_open)
    def test_post_success(self, mock_open):
        # Mock request data
        data = {"alert_spread": 0.5}
        mid = "test_market"
        url = reverse(
            "alert_spread_polling", kwargs={"mid": mid}
        )  # Adjust this to match your URL configuration

        # Perform the POST request
        response = self.client.post(url, data)

        # Check that the file was attempted to be opened
        mock_open.assert_called_with(f"{mid}_alert_spread.json", "w+")

        # Assert response status code and content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "mid": mid,
                "alert_spread": 0.5,
                "status": "created",
            },
        )

    @patch("builtins.open", new_callable=mock_open)
    def test_post_error_invalid_value(self, mock_open):
        # Mock request data with an invalid alert_spread value
        data = {"alert_spread": "invalid_float"}
        mid = "test_market"
        url = reverse(
            "alert_spread_polling", kwargs={"mid": mid}
        )  # Adjust this to match your URL configuration

        # Perform the POST request
        response = self.client.post(url, data)

        # Check that the file operation was not performed
        mock_open.assert_not_called()

        # Assert response status code and content
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.data)
