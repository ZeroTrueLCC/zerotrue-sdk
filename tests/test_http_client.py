"""Tests for HTTP client."""

import pytest

import zerotrue.http_client as http_mod
from zerotrue.http_client import DEFAULT_API_BASE_URL, HTTPClient


def test_http_client_initialization():
    """Test HTTP client initialization."""
    client = HTTPClient(api_key="test_key")
    assert client.api_key == "test_key"
    assert client.base_url == DEFAULT_API_BASE_URL


def test_http_client_custom_options(monkeypatch: pytest.MonkeyPatch):
    """Timeout/retry options (URL is the SDK constant; patch only for this assertion)."""
    monkeypatch.setattr(http_mod, "DEFAULT_API_BASE_URL", "https://custom.url")
    client = HTTPClient(
        api_key="test_key",
        timeout=60000,
        max_retries=5,
        retry_delay=2000,
        debug=True,
    )
    assert client.base_url == "https://custom.url"
    assert client.timeout == 60.0
    assert client.max_retries == 5
    assert client.retry_delay == 2.0
