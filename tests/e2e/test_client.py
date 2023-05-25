from typing import Dict, List

from openweathermappy.client import OpenWeatherMapClient

from tests.base_tests import BaseE2ETest


class TestE2EOpenWeatherMapClient(BaseE2ETest):
    def test_getNameOfLocationUsingLatitudeAndLongitude(
            self,
            clientFromDotEnv: OpenWeatherMapClient
        ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getNameOfLocationUsingLatitudeAndLongitude(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None
        assert isinstance(sut, List)
        for item in sut:
            assert item is not None
            assert isinstance(item, Dict)

    def test_getWeatherUsingOneCallAPI(
            self,
            clientFromDotEnv: OpenWeatherMapClient
        ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getWeatherUsingOneCallAPI(
            latitude=17.69,
            longitude=83.2093,
            exclude=list()
        )
        # Assert
        assert sut is not None