"""Example of cancelling wait operation using signal."""

import os
import threading

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from zerotrue import ZeroTrue

client = ZeroTrue(
    api_key=os.getenv("ZEROTRUE_API_KEY", "zt_your_api_key_here"),
)

# Create a cancellation signal (similar to AbortSignal in Node.js)
cancel_signal = threading.Event()

# Start check
check = client.checks.create(
    {
        "input": {"type": "text", "value": "Check this text..."},
    }
)


# In another thread, you can cancel the operation after 10 seconds
def cancel_after_timeout():
    import time

    time.sleep(10)
    cancel_signal.set()
    print("Operation cancelled!")


threading.Thread(target=cancel_after_timeout, daemon=True).start()

# Wait for result with cancellation support
try:
    result = client.checks.wait(
        check["id"],
        {
            "pollInterval": 2000,
            "maxPollTime": 300000,
            "signal": cancel_signal,  # Pass signal for cancellation
        },
    )
    print(f"Result: {result}")
except InterruptedError as e:
    print(f"Wait was cancelled: {e}")
