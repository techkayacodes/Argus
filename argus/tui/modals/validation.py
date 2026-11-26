"""Shared validation helpers for TUI modals."""

from __future__ import annotations

import math

BUDGET_MIN_USD = 0.01
BUDGET_MAX_USD = 10.0
BUDGET_RANGE_TEXT = f"${BUDGET_MIN_USD:.2f} – ${BUDGET_MAX_USD:.2f}"


def validate_budget_ceiling(raw: str) -> float:
    """Parse and validate a USD budget ceiling string.

    Accepts optional `$` and `USD` decorations and enforces the unified
    [BUDGET_MIN_USD, BUDGET_MAX_USD] range. Raises ValueError on invalid input.
    """
    cleaned = raw.replace("$", "").replace("USD", "").strip()
    try:
        value = float(cleaned)
    except ValueError as exc:
        raise ValueError("Invalid budget number format") from exc

    if not math.isfinite(value) or not (BUDGET_MIN_USD <= value <= BUDGET_MAX_USD):
        raise ValueError(
            f"Budget must be between ${BUDGET_MIN_USD:.2f} and ${BUDGET_MAX_USD:.2f} USD"
        )
    return value
