"""Самый простой пример - БЕЗ idempotencyKey и лишних параметров."""

import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from zerotrue import ZeroTrue

# Инициализация клиента
client = ZeroTrue(api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here"))

# Пример 1: Проверка текста (минимальный код, БЕЗ idempotencyKey)
result = client.checks.create_and_wait(
    {
        "input": {"type": "text", "value": "This is a text to check for AI generation."},
    }
)

print(f"AI Probability: {result.get('ai_probability', 0)}%")

# Пример 2: Создание проверки БЕЗ idempotencyKey
check = client.checks.create(
    {
        "input": {"type": "text", "value": "Another text example"},
    }
)

# Ждем результат
result = client.checks.wait(check["id"])
print(f"Result: {result.get('result_type', 'unknown')}")

# Пример 3: Проверка URL - тоже БЕЗ idempotencyKey
url_result = client.checks.create_and_wait(
    {
        "input": {"type": "url", "value": "https://example.com/image.png"},
    }
)

print(f"URL check: {url_result.get('result_type', 'unknown')}")

# ВАЖНО: idempotencyKey НЕ обязателен!
# Все примеры выше работают без него.
# Используй idempotencyKey только если нужна защита от дубликатов при retry.
