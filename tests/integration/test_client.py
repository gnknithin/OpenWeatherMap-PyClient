import os

import pytest

from openweathermappy.client import OpenWeatherMapClient
from openweathermappy.core.constants import ClientEnvironmentVariable
from tests.base_tests import BaseIntegrationTest


class TestOpenWeatherMapClient(BaseIntegrationTest):
    INVALID_OPENWEATHERMAP_API_KEY = 'dummy-api-key'

    def test_should_raise_type_error(self) -> None:
        with pytest.raises(TypeError) as type_err:
            # Arrange
            # Act
            OpenWeatherMapClient()  # type: ignore
            # Assert
            assert type_err.type is TypeError

    def test_should_return_an_instance_properly(self) -> None:
        # Arrange
        # Act
        sut = OpenWeatherMapClient(
            apiKey=self.INVALID_OPENWEATHERMAP_API_KEY
        )
        # Assert
        assert sut is not None
        assert isinstance(sut, OpenWeatherMapClient)

    @pytest.mark.xfail(reason="if .env file is not available")  # type: ignore
    def test_should_load_from_dotenv_file_and_return_an_instance_properly(self) -> None:
        # Arrange
        # Act
        sut = OpenWeatherMapClient.loadFromDotEnvFile()
        # Assert
        assert sut is not None
        assert isinstance(sut, OpenWeatherMapClient)

    @pytest.mark.xfail(reason="if environemnt varaible is not set")
    def test_should_load_from_environment_and_return_an_instance_properly(self) -> None:
        # Arrange
        os.putenv(
            ClientEnvironmentVariable.OPENWEATHERMAP_API_KEY,
            "HELLODUMMYKEY"
        )
        # Act
        sut = OpenWeatherMapClient.loadFromEnvironmentVariable()
        # Assert
        assert sut is not None
        assert isinstance(sut, OpenWeatherMapClient)
        # Clean-Up
        beforeCleanUp = os.getenv(
            ClientEnvironmentVariable.OPENWEATHERMAP_API_KEY
        )
        assert beforeCleanUp is not None
        os.environ.pop(ClientEnvironmentVariable.OPENWEATHERMAP_API_KEY)
        afterCleanUp = os.getenv(
            ClientEnvironmentVariable.OPENWEATHERMAP_API_KEY)
        assert afterCleanUp is None
