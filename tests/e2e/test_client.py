from datetime import datetime
from random import randint

from openweathermappy.client import OpenWeatherMapClient

from tests.base_tests import BaseE2ETest


class TestE2EOpenWeatherMapClient(BaseE2ETest):

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

    def test_getHistoricalWeatherUsingOneCallAPI(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHistoricalWeatherUsingOneCallAPI(
            latitude=17.69,
            longitude=83.2093,
            exclude=list()
        )
        # Assert
        assert sut is not None

    def test_getCurrentWeatherDataFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getCurrentWeatherDataFromLatitudeAndLongitude(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getCurrentWeatherDataByCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getCurrentWeatherDataByCityName(
            cityName="visakhapatnam"
        )
        # Assert
        assert sut is not None

    def test_getCurrentWeatherDataByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getCurrentWeatherDataByCityId(
            cityId=1253102
        )
        # Assert
        assert sut is not None

    def test_getCurrentWeatherDataByZipCode(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getCurrentWeatherDataByZipCode(
            zipCode=530003,
            countryCode="IN"
        )
        # Assert
        assert sut is not None

    def test_getHourlyForcastFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHourlyForcastFromLatitudeAndLongitude(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getHourlyForcastFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHourlyForcastFromCityName(
            cityName="visakhapatnam"
        )
        # Assert
        assert sut is not None

    def test_getHourlyForcastByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHourlyForcastByCityId(
            cityId=1253102
        )
        # Assert
        assert sut is not None

    def test_getHourlyForcastByZipCode(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHourlyForcastByZipCode(
            zipCode=530003,
            countryCode="IN"
        )
        # Assert
        assert sut is not None

    def test_getDailyForcastFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getDailyForcastFromLatitudeAndLongitude(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getDailyForcastFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getDailyForcastFromCityName(
            cityName="visakhapatnam"
        )
        # Assert
        assert sut is not None

    def test_getDailyForcastByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getDailyForcastByCityId(
            cityId=1253102
        )
        # Assert
        assert sut is not None

    def test_getDailyForcastByZipCode(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getDailyForcastByZipCode(
            zipCode=530003,
            countryCode="IN"
        )
        # Assert
        assert sut is not None

    def test_getClimateForcastFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getClimateForcastFromLatitudeAndLongitude(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getClimateForcastFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getClimateForcastFromCityName(
            cityName="visakhapatnam"
        )
        # Assert
        assert sut is not None

    def test_getClimateForcastByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getClimateForcastByCityId(
            cityId=1253102
        )
        # Assert
        assert sut is not None

    def test_getClimateForcastByZipCode(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getClimateForcastByZipCode(
            zipCode=530003,
            countryCode="IN"
        )
        # Assert
        assert sut is not None

    def test_getWeatherForcastFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getWeatherForcastFromLatitudeAndLongitude(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getWeatherForcastFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getWeatherForcastFromCityName(
            cityName="visakhapatnam"
        )
        # Assert
        assert sut is not None

    def test_getWeatherForcastByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getWeatherForcastByCityId(
            cityId=1253102
        )
        # Assert
        assert sut is not None

    def test_getWeatherForcastByZipCode(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getWeatherForcastByZipCode(
            zipCode=530003,
            countryCode="IN"
        )
        # Assert
        assert sut is not None

    def test_getHourlyHistoricalDataFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHourlyHistoricalDataFromLatitudeAndLongitude(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getHourlyHistoricalDataFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHourlyHistoricalDataFromCityName(
            cityName="visakhapatnam"
        )
        # Assert
        assert sut is not None

    def test_getHourlyHistoricalDataByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHourlyHistoricalDataByCityId(
            cityId=1253102
        )
        # Assert
        assert sut is not None

    def test_getHistoricalDataByTimestampFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getHistoricalDataByTimestampFromLatitudeAndLongitude(
            latitude=17.69,
            longitude=83.2093,
            dt=datetime.utcnow().timestamp()
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedYearlyFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = getattr(
            clientFromDotEnv,
            "getStatisticalWeatherAggregatedYearlyFromLatitudeAndLongitude"
        )(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedYearlyFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getStatisticalWeatherAggregatedYearlyFromCityName(
            cityName="visakhapatnam"
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedYearlyByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getStatisticalWeatherAggregatedYearlyByCityId(
            cityId=1253102
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedMonthlyFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = getattr(
            clientFromDotEnv,
            "getStatisticalWeatherAggregatedMonthlyFromLatitudeAndLongitude"
        )(
            latitude=17.69,
            longitude=83.2093,
            month=randint(1, 13)
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedMonthlyFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getStatisticalWeatherAggregatedMonthlyFromCityName(
            cityName="visakhapatnam",
            month=randint(1, 13)
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedMonthlylyByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getStatisticalWeatherAggregatedMonthlyByCityId(
            cityId=1253102,
            month=randint(1,13)
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedDailyFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = getattr(
            clientFromDotEnv,
            "getStatisticalWeatherAggregatedDailyFromLatitudeAndLongitude"
        )(
            latitude=17.69,
            longitude=83.2093,
            month=randint(1, 13),
            day=randint(1, 31)
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedDailyFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getStatisticalWeatherAggregatedDailyFromCityName(
            cityName="visakhapatnam",
            month=randint(1, 13),
            day=randint(1,31)
        )
        # Assert
        assert sut is not None

    def test_getStatisticalWeatherAggregatedDailylyByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getStatisticalWeatherAggregatedDailyByCityId(
            cityId=1253102,
            month=randint(1,13),
            day=randint(1,31)
        )
        # Assert
        assert sut is not None

    def test_getAccumulatedTemperatureFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = getattr(
            clientFromDotEnv,
            "getAccumulatedTemperatureFromLatitudeAndLongitude"
        )(
            latitude=17.69,
            longitude=83.2093,
            start=datetime.utcnow().timestamp(),
            end=datetime.utcnow().timestamp(),
            threshold=randint(1, 100)
        )
        # Assert
        assert sut is not None

    def test_getAccumulatedTemperatureFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getAccumulatedTemperatureFromCityName(
            cityName="visakhapatnam",
            countryCode="IN",
            start=datetime.utcnow().timestamp(),
            end=datetime.utcnow().timestamp(),
            threshold=randint(1, 100)
        )
        # Assert
        assert sut is not None

    def test_getAccumulatedTemperatureByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getAccumulatedTemperatureByCityId(
            cityId=1253102,
            start=datetime.utcnow().timestamp(),
            end=datetime.utcnow().timestamp(),
            threshold=randint(1, 100)
        )
        # Assert
        assert sut is not None

    def test_getAccumulatedPrecipitationFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = getattr(
            clientFromDotEnv,
            "getAccumulatedPrecipitationFromLatitudeAndLongitude"
        )(
            latitude=17.69,
            longitude=83.2093,
            start=datetime.utcnow().timestamp(),
            end=datetime.utcnow().timestamp(),
            threshold=randint(1, 100)
        )
        # Assert
        assert sut is not None

    def test_getAccumulatedPrecipitationFromCityName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getAccumulatedPrecipitationFromCityName(
            cityName="visakhapatnam",
            countryCode="IN",
            start=datetime.utcnow().timestamp(),
            end=datetime.utcnow().timestamp(),
            threshold=randint(1, 100)
        )
        # Assert
        assert sut is not None

    def test_getAccumulatedPrecipitationByCityId(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getAccumulatedPrecipitationByCityId(
            cityId=1253102,
            start=datetime.utcnow().timestamp(),
            end=datetime.utcnow().timestamp(),
            threshold=randint(1, 100)
        )
        # Assert
        assert sut is not None

    def test_getAirPollutionForecastDataFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = getattr(
            clientFromDotEnv,
            "getAirPollutionForecastDataFromLatitudeAndLongitude"
        )(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getAirPollutionHistoricalDataFromLatitudeAndLongitude(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = getattr(
            clientFromDotEnv,
            "getAirPollutionHistoricalDataFromLatitudeAndLongitude"
        )(
            latitude=17.69,
            longitude=83.2093
        )
        # Assert
        assert sut is not None

    def test_getCoordinatesByLocationName(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getCoordinatesByLocationName(
            cityName="visakhapatnam",
            countryCode="IN"
        )
        # Assert
        assert sut is not None

    def test_getCoordinatesByZipCode(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getCoordinatesByZipCode(
            zipCode=530003,
            countryCode="IN"
        )
        # Assert
        assert sut is not None

    def test_getCoordinatesByPostalCode(
        self,
        clientFromDotEnv: OpenWeatherMapClient
    ):
        # Arrange
        # Act
        sut = clientFromDotEnv.getCoordinatesByPostalCode(
            postalCode=530003,
            countryCode="IN"
        )
        # Assert
        assert sut is not None

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
