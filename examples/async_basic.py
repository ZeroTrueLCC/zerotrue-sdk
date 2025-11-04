"""Basic async usage example for ZeroTrue SDK."""

import asyncio
import os

from zerotrue import AsyncZeroTrue


async def main():
    # Initialize async client
    client = AsyncZeroTrue(
        api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here"),
    )

    try:
        # Example 1: Async check text for AI generation
        result = await client.checks.create_and_wait(
            {
                "input": {"type": "text", "value": "Check this text..."},
            }
        )

        print(f"AI Probability: {result.get('ai_probability', 0)}%")
        print(f"Result: {result.get('result_type', 'unknown')}")

        # Example 2: Create check and wait separately
        check = await client.checks.create(
            {
                "input": {"type": "text", "value": "Another text to check"},
            }
        )

        print(f"Check ID: {check['id']}")

        # Wait for result
        result = await client.checks.wait(check["id"])
        print(f"Status: {result['status']}")

    finally:
        # Close the client
        await client.close()


# Alternative: Using async context manager
async def main_with_context():
    async with AsyncZeroTrue(api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here")) as client:
        result = await client.checks.create_and_wait(
            {
                "input": {"type": "text", "value": "Check this text..."},
            }
        )
        print(f"AI Probability: {result.get('ai_probability', 0)}%")


if __name__ == "__main__":
    # Run async main
    asyncio.run(main())

    # Or with context manager
    # asyncio.run(main_with_context())
