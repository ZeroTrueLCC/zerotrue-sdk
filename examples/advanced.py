"""Advanced usage examples for ZeroTrue SDK."""

import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from zerotrue import ZeroTrue

client = ZeroTrue(
    api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here"),
    base_url="https://app.zerotrue.app",
    timeout=30000,
    max_retries=3,
    retry_delay=1000,
    debug=False,
)

# Example 1: Create check and retrieve separately
check = client.checks.create(
    {
        "input": {
            "type": "text",
            "value": "Your text to analyze...",
        },
        "isPrivateScan": True,
        "isDeepScan": False,
    }
)

# Get result
result = client.checks.retrieve(check["id"])

# Example 2: Wait for completion with custom options
result = client.checks.wait(
    check["id"],
    {
        "pollInterval": 2000,  # 2 seconds
        "maxPollTime": 300000,  # 5 minutes
    },
)

# Example 3: Check URL
check = client.checks.create(
    {
        "input": {
            "type": "url",
            "value": "https://example.com/image.png",
        },
    }
)

# Example 4: Работа БЕЗ idempotencyKey (самый простой способ)
check_simple = client.checks.create(
    {
        "input": {"type": "text", "value": "Test without key"},
        # idempotencyKey НЕ указан - всё работает отлично!
    }
)
print(f"Simple check ID: {check_simple['id']}")

# Example 5: Idempotency (ОПЦИОНАЛЬНО, только для защиты от дубликатов)
# Используй idempotencyKey ТОЛЬКО если нужно избежать повторных создаваний
check = client.checks.create(
    {
        "input": {"type": "text", "value": "Test"},
        "idempotencyKey": "unique-request-id-123",  # Опциональный параметр
    }
)

# Повторный запрос с тем же ключом вернет тот же результат (без создания нового)
check2 = client.checks.create(
    {
        "input": {"type": "text", "value": "Test"},
        "idempotencyKey": "unique-request-id-123",
    }
)

print(f"Same check ID: {check['id'] == check2['id']}")  # True
