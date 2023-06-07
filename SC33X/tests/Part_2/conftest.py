import os
import csv
import pytest

@pytest.fixture
def get_app():
    from sprint_challenge.Part_2 import app
    return app
