from abc import ABC
from typing import Optional

import pytest

from openweathermappy.client import OpenWeatherMapClient


class BaseIntegrationTest(ABC):
    pytestmark = pytest.mark.integration


class BaseE2ETest(ABC):
    pytestmark = pytest.mark.e2e

    @pytest.fixture(autouse=True)
    def clientFromDotEnv(self) -> Optional['OpenWeatherMapClient']:
        return OpenWeatherMapClient.loadFromDotEnvFile()
