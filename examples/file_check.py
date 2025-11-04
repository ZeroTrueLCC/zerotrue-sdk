"""File upload examples for ZeroTrue SDK."""

import os

from zerotrue import ZeroTrue

client = ZeroTrue(
    api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here"),
)

# Example 1: Check file from path
check = client.checks.create_from_file(
    "./image.png",
    {
        "isPrivateScan": True,
        "isDeepScan": False,
    },
)

# Get result
result = client.checks.retrieve(check["id"])
print(f"Check ID: {result['id']}")
print(f"Status: {result['status']}")

# Example 2: Check file from buffer
with open("./image.png", "rb") as f:
    check = client.checks.create_from_buffer(f, "image.png")

# Wait for completion
result = client.checks.wait(check["id"])
print(f"AI Probability: {result.get('ai_probability', 0)}%")

# Example 3: Check from bytes
with open("./image.png", "rb") as f:
    file_bytes = f.read()

check = client.checks.create_from_buffer(file_bytes, "image.png")
result = client.checks.wait(check["id"])
print(f"Result type: {result.get('result_type', 'unknown')}")
