"""Error handling examples for ZeroTrue SDK."""

from zerotrue import ZeroTrue
from zerotrue.exceptions import APIError, AuthenticationError, RateLimitError, ValidationError

client = ZeroTrue(
    api_key="zt_your_api_key_here",
)

try:
    check = client.checks.create(
        {
            "input": {"type": "text", "value": "Test"},
        }
    )
except ValidationError as e:
    print(f"Validation failed: {e}")
except AuthenticationError as e:
    print(f"Invalid API key: {e}")
except RateLimitError as e:
    print(f"Rate limit exceeded. Retry after: {e.retry_after} seconds")
except APIError as e:
    print(f"API error: {e}")
    print(f"Status code: {e.status_code}")
except Exception as e:
    print(f"Unknown error: {e}")
