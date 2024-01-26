"""
Pytest Fixtures Shared Across all Unit Tests
"""

import os
import pathlib

import pytest
from vcr import VCR


@pytest.fixture(autouse=True)
def set_test_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Set Environment Variables for Testing if they are not already set
    """
    testing_env_vars = [
        "LUNCHMONEY_ACCESS_TOKEN",
        "SPLITWISE_API_KEY",
        "SPLITWISE_CONSUMER_KEY",
        "SPLITWISE_CONSUMER_SECRET",
    ]
    for env_var in testing_env_vars:
        if not os.getenv(env_var):
            monkeypatch.setenv(env_var, f"{env_var}_PLACEHOLDER")


def path_transformer(path: str) -> str:
    """
    Cassette Path Transformer
    """
    suffix = ".yaml"
    if not path.endswith(suffix):
        path = path + suffix
    cassette_path = pathlib.Path(path)
    cassette_path = cassette_path.parent / "cassettes" / cassette_path.name
    return str(cassette_path)


vcr = VCR(
    filter_headers=(("authorization", "XXXXXXXXXX"),),
    filter_query_parameters=(("user", "XXXXXXXXXX"), ("token", "XXXXXXXXXX")),
    path_transformer=path_transformer,
    record_mode=os.getenv("VCR_RECORD_MODE", "once"),
)

# Decorator Object to Use pyvcr Cassettes on Unit Tests
# pass `--vcr-record=none` to pytest CI runs to ensure new cassettes are generated
lunchable_cassette = vcr.use_cassette
