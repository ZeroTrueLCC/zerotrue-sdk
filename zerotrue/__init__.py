"""ZeroTrue Python SDK - Official SDK for ZeroTrue AI Detection API."""

from zerotrue.async_client import AsyncZeroTrue
from zerotrue.client import ZeroTrue
from zerotrue.exceptions import APIError, AuthenticationError, RateLimitError, ValidationError

__version__ = "1.3.1"
__all__ = [
    "ZeroTrue",
    "AsyncZeroTrue",
    "APIError",
    "AuthenticationError",
    "RateLimitError",
    "ValidationError",
]
