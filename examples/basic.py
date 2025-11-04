"""Basic usage example for ZeroTrue SDK."""

import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from zerotrue import ZeroTrue

# Initialize client
client = ZeroTrue(
    api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here"),
)

# Example 1: Простейший способ - БЕЗ дополнительных параметров
result = client.checks.create_and_wait(
    {
        "input": {"type": "text", "value": "Check this text..."},
        # idempotencyKey НЕ указан - всё работает!
    }
)

print(f"AI Probability: {result.get('ai_probability', 0)}%")
print(f"Result: {result.get('result_type', 'unknown')}")

# Example 2: Создание проверки БЕЗ idempotencyKey
check = client.checks.create(
    {
        "input": {"type": "text", "value": "Another text to check"},
        # idempotencyKey НЕ нужен!
    }
)

print(f"Check ID: {check['id']}")
print(f"Status: {check['status']}")
