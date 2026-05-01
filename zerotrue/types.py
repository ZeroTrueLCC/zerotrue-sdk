"""Type definitions for ZeroTrue SDK."""

from typing import Any, Dict, List, Literal, Optional, TypedDict

CheckStatus = Literal["queued", "processing", "completed", "failed", "canceled", "expired"]


class InputDict(TypedDict):
    """Input dictionary for check creation."""

    type: Literal["text", "url"]
    value: str


class CheckResponse(TypedDict):
    """Response from check creation."""

    id: str
    status: CheckStatus


class SuspectedModel(TypedDict, total=False):
    """Suspected AI model information."""

    model_name: str
    confidence_pct: Optional[float]


class Segment(TypedDict, total=False):
    """Segment information for detailed analysis."""

    label: Optional[str]
    confidence_pct: Optional[float]
    start_char: Optional[int]
    end_char: Optional[int]
    start_line: Optional[int]
    end_line: Optional[int]
    start_s: Optional[float]
    end_s: Optional[float]
    timecode: Optional[str]


class CheckResult(CheckResponse, total=False):
    """Extended check result with analysis data."""

    created_at: Optional[str]
    ai_probability: Optional[float]
    human_probability: Optional[float]
    combined_probability: Optional[float]
    result_type: Optional[str]
    ml_model: Optional[str]
    ml_model_version: Optional[str]
    details: Optional[Dict[str, Any]]
    feedback: Optional[str]
    status: Optional[str]
    file_url: Optional[str]
    original_filename: Optional[str]
    size_bytes: Optional[int]
    size_mb: Optional[float]
    resolution: Optional[str]
    length: Optional[int]
    content: Optional[str]
    is_private_scan: Optional[bool]
    is_deep_scan: Optional[bool]
    price: Optional[int]
    inference_time_ms: Optional[int]
    api_schema_version: Optional[str]
    meta_mime: Optional[str]
    meta_file_size_bytes: Optional[int]
    meta_sha256: Optional[str]
    meta_content_url: Optional[str]
    meta_content_type: Optional[str]
    details_summary: Optional[Dict[str, Any]]
    details_extra: Optional[Dict[str, Any]]
    suspected_models: Optional[List[SuspectedModel]]
    segments: Optional[List[Segment]]
    metadata: Optional[Dict[str, Any]]


class CreateCheckParams(TypedDict, total=False):
    """Parameters for creating a check."""

    input: InputDict
    isPrivateScan: bool
    isDeepScan: bool
    idempotencyKey: Optional[str]
    metadata: Optional[Dict[str, Any]]


class WaitOptions(TypedDict, total=False):
    """Options for waiting for check completion."""

    pollInterval: int
    maxPollTime: int
    signal: Any  # For cancellation support (similar to AbortSignal)
