"""Unit tests for unified budget ceiling validation across PolicyModal and ConfigModal."""

from __future__ import annotations

import pytest

from argus.tui.modals.validation import (
    BUDGET_MAX_USD,
    BUDGET_MIN_USD,
    BUDGET_RANGE_TEXT,
    validate_budget_ceiling,
)


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("0.01", 0.01),
        ("5.00", 5.0),
        ("7.50", 7.5),
        ("10.00", 10.0),
        ("$10.00", 10.0),
        ("$0.01 USD", 0.01),
        ("  6.25 USD ", 6.25),
    ],
)
def test_validate_budget_ceiling_accepts_unified_range(raw: str, expected: float) -> None:
    assert validate_budget_ceiling(raw) == pytest.approx(expected)


@pytest.mark.parametrize(
    "raw",
    [
        "",
        "0",
        "0.00",
        "0.009",
        "-1.0",
        "10.01",
        "100",
        "abc",
        "nan",
        "inf",
        "-inf",
    ],
)
def test_validate_budget_ceiling_rejects_out_of_range_and_invalid(raw: str) -> None:
    with pytest.raises(ValueError):
        validate_budget_ceiling(raw)


def test_budget_bounds_constants() -> None:
    assert BUDGET_MIN_USD == 0.01
    assert BUDGET_MAX_USD == 10.0
    assert "$0.01" in BUDGET_RANGE_TEXT and "$10.00" in BUDGET_RANGE_TEXT
