"""Pytest configuration for pipup tests."""

import pytest


# Add the pytest-mock fixture if not automatically available
@pytest.fixture
def mocker():
    """Return a mock object that can be used to mock functions."""
    try:
        import pytest_mock
        pytest_mock_fixture = pytest.importorskip("pytest_mock").MockFixture
        return pytest_mock_fixture(request=pytest.request)
    except ImportError:
        # Fallback if pytest-mock is not installed
        from unittest import mock
        return mock 