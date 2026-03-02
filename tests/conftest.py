import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(autouse=True)
def isolate_activities():
    """Make a deep copy of the in-memory `activities` before each test and restore after.

    This keeps tests isolated from each other's mutations.
    """
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)


@pytest.fixture
def client():
    """Sync TestClient fixture for endpoint tests."""
    return TestClient(app)
