"""Parallel async requests example - main advantage of async."""

import asyncio
import os

from zerotrue import AsyncZeroTrue


async def check_multiple_texts():
    """Check multiple texts in parallel."""
    async with AsyncZeroTrue(api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here")) as client:
        texts = [
            "First text to check for AI generation",
            "Second text to analyze",
            "Third piece of content",
            "Fourth sample text",
            "Fifth text example",
        ]

        # Create all checks in parallel
        print("Creating checks in parallel...")
        tasks = [
            client.checks.create_and_wait(
                {
                    "input": {"type": "text", "value": text},
                }
            )
            for text in texts
        ]

        # Wait for all to complete
        results = await asyncio.gather(*tasks)

        # Print results
        for i, result in enumerate(results, 1):
            print(f"\nText {i}:")
            print(f"  AI Probability: {result.get('ai_probability', 0)}%")
            print(f"  Result: {result.get('result_type', 'unknown')}")


async def check_mixed_content():
    """Check text, URLs, and files in parallel."""
    async with AsyncZeroTrue(api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here")) as client:
        # Mix of different check types
        tasks = [
            # Text check
            client.checks.create_and_wait(
                {
                    "input": {"type": "text", "value": "Sample text"},
                }
            ),
            # URL check
            client.checks.create_and_wait(
                {
                    "input": {"type": "url", "value": "https://example.com/image.png"},
                }
            ),
            # Another text
            client.checks.create_and_wait(
                {
                    "input": {"type": "text", "value": "Another sample"},
                }
            ),
        ]

        # All run in parallel!
        results = await asyncio.gather(*tasks)

        print(f"Completed {len(results)} checks in parallel")
        for result in results:
            print(f"  - {result['id']}: {result.get('result_type', 'unknown')}")


async def check_with_progress():
    """Check multiple items with progress reporting."""
    async with AsyncZeroTrue(api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here")) as client:
        texts = [f"Sample text number {i}" for i in range(10)]

        # Create all checks
        check_tasks = [client.checks.create({"input": {"type": "text", "value": text}}) for text in texts]

        checks = await asyncio.gather(*check_tasks)
        print(f"Created {len(checks)} checks")

        # Wait for all with progress
        async def wait_with_progress(check_id, index):
            result = await client.checks.wait(check_id)
            print(f"✓ Check {index + 1}/{len(checks)} completed")
            return result

        wait_tasks = [wait_with_progress(check["id"], i) for i, check in enumerate(checks)]

        results = await asyncio.gather(*wait_tasks)
        print(f"\n✅ All {len(results)} checks completed!")


if __name__ == "__main__":
    print("Example 1: Check multiple texts in parallel")
    asyncio.run(check_multiple_texts())

    print("\n" + "=" * 50 + "\n")

    print("Example 2: Check mixed content types in parallel")
    asyncio.run(check_mixed_content())

    print("\n" + "=" * 50 + "\n")

    print("Example 3: Check with progress reporting")
    asyncio.run(check_with_progress())
