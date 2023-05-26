import os
from typing import Any, Dict, List, Optional

import dotenv

from .core.constants import ClientEnvironmentVariable, ErrorMessage
from .core.manager import ContextManager


class OpenWeatherMapClient:
    def __init__(self, apiKey: str) -> None:
        self._context = ContextManager(api_key=apiKey)

    @classmethod
    def loadFromEnvironmentVariable(cls) -> Optional['OpenWeatherMapClient']:
        _apiKey = os.environ.get(
            ClientEnvironmentVariable.OPENWEATHERMAP_API_KEY
        )
        if _apiKey is None:
            raise ValueError(ErrorMessage.INITIALIZATION_FAILURE)
        return cls(_apiKey)

    @classmethod
    def loadFromDotEnvFile(cls) -> Optional['OpenWeatherMapClient']:
        dotenv.load_dotenv(dotenv_path=dotenv.find_dotenv())
        return OpenWeatherMapClient.loadFromEnvironmentVariable()

    def getWeatherUsingOneCallAPI(
            self,
            latitude: float,
            longitude: float,
            exclude:List[str],
            units: str = "standard",
            lang:Optional[str]=None
        )->Any:
        return self._context.fetchWeatherOneCallAPI(
            lat=latitude,
            lon=longitude,
            exclude=exclude,
            units=units,
            language=lang,
        ).json()

    def getHistoricalWeatherUsingOneCallAPI(
            self,
            latitude: float,
            longitude: float,
            exclude:List[str],
            units: str = "standard",
            lang:Optional[str]=None
        )->Any:
        return self._context.fetchHistoricalWeatherOneCallAPI(
            lat=latitude,
            lon=longitude,
            exclude=exclude,
            units=units,
            language=lang,
        ).json()

    def getCurrentWeatherDataFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        units: str = "standard",
        lang:Optional[str]=None
    ) -> Any:
        return self._context.fetchCurrentWeatherByCoordinates(
            lat=latitude,
            lon=longitude,
            units=units,
            language=lang
        ).json()

    def getCurrentWeatherDataByCityName(
        self,
        cityName: str,
        stateCode: Optional[str] = None,
        countryCode: Optional[str] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Dict[Any, Any]:
        return self._context.fetchCurrentWeatherByCityName(
            cityName=cityName,
            stateCode=stateCode,
            countryCode=countryCode,
            units=units,
            language=lang
        ).json()

    def getCurrentWeatherDataByCityId(
        self,
        cityId: int,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Dict[Any, Any]:
        return self._context.fetchCurrentWeatherByCityId(
            cityId=cityId,
            units=units,
            language=lang
        ).json()

    def getCurrentWeatherDataByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str]=None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Dict[Any, Any]:
        return self._context.fetchCurrentWeatherByZipCode(
            zipCode=zipCode,
            countryCode=countryCode,
            units=units,
            language=lang
        ).json()

    def getHourlyForcastFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        cnt: Optional[int]=None,
        lang:Optional[str]=None
    ) -> Any:
        return self._context.fetchHourlyForcastByCoordinates(
            lat=latitude,
            lon=longitude,
            cnt=cnt,
            language=lang
        ).json()

    def getHourlyForcastFromCityName(
        self,
        cityName: str,
        stateCode: Optional[str] = None,
        countryCode: Optional[str] = None,
        cnt: Optional[int] = None,
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchHourlyForcastByCityName(
            cityName=cityName,
            stateCode=stateCode,
            countryCode=countryCode,
            cnt=cnt,
            language=lang
        ).json()

    def getHourlyForcastByCityId(
        self,
        cityId: int,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchHourlyForcastByCityId(
            cityId=cityId,
            units=units,
            language=lang
        ).json()

    def getHourlyForcastByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchHourlyForcastByZipCode(
            zipCode=zipCode,
            countryCode=countryCode,
            units=units,
            language=lang
        ).json()

    def getDailyForcastFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchDailyForcastByCoordinates(
            lat=latitude,
            lon=longitude,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getDailyForcastFromCityName(
        self,
        cityName: str,
        stateCode: Optional[str] = None,
        countryCode: Optional[str] = None,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchDailyForcastByCityName(
            cityName=cityName,
            stateCode=stateCode,
            countryCode=countryCode,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getDailyForcastByCityId(
        self,
        cityId: int,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchDailyForcastByCityId(
            cityId=cityId,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getDailyForcastByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str] = None,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchDailyForcastByZipCode(
            zipCode=zipCode,
            countryCode=countryCode,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getClimateForcastFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchClimateForcastByCoordinates(
            lat=latitude,
            lon=longitude,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getClimateForcastFromCityName(
        self,
        cityName: str,
        countryCode: Optional[str] = None,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchClimateForcastByCityName(
            cityName=cityName,
            countryCode=countryCode,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getClimateForcastByCityId(
        self,
        cityId: int,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchClimateForcastByCityId(
            cityId=cityId,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getClimateForcastByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str] = None,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchClimateForcastByZipCode(
            zipCode=zipCode,
            countryCode=countryCode,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getWeatherForcastFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchWeatherForcastByCoordinates(
            lat=latitude,
            lon=longitude,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getWeatherForcastFromCityName(
        self,
        cityName: str,
        stateCode: Optional[str] = None,
        countryCode: Optional[str] = None,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchWeatherForcastByCityName(
            cityName=cityName,
            stateCode=stateCode,
            countryCode=countryCode,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getWeatherForcastByCityId(
        self,
        cityId: int,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchWeatherForcastByCityId(
            cityId=cityId,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getWeatherForcastByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str] = None,
        cnt: Optional[int] = None,
        units: str = "standard",
        lang: Optional[str] = None
    ) -> Any:
        return self._context.fetchWeatherForcastByZipCode(
            zipCode=zipCode,
            countryCode=countryCode,
            cnt=cnt,
            units=units,
            language=lang
        ).json()

    def getHourlyHistoricalDataFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        start: Optional[float] = None,
        end: Optional[float] = None,
        cnt: Optional[int] = None
    ) -> Any:
        return self._context.fetchHourlyHistoricalDataByCoordinates(
            lat=latitude,
            lon=longitude,
            start=start,
            end=end,
            cnt=cnt
        ).json()

    def getHourlyHistoricalDataFromCityName(
        self,
        cityName: str,
        countryCode: Optional[str] = None,
        start: Optional[float] = None,
        end: Optional[float] = None,
        cnt: Optional[int] = None
    ) -> Any:
        return self._context.fetchHourlyHistoricalDataByCityName(
            cityName=cityName,
            countryCode=countryCode,
            start=start,
            end=end,
            cnt=cnt
        ).json()

    def getHourlyHistoricalDataByCityId(
        self,
        cityId: int,
        start: Optional[float] = None,
        end: Optional[float] = None,
        cnt: Optional[int] = None,
    ) -> Any:
        return self._context.fetchHourlyHistoryDataByCityId(
            cityId=cityId,
            start=start,
            end=end,
            cnt=cnt
        ).json()

    def getHistoricalDataByTimestampFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        dt: float,
    ) -> Any:
        return self._context.fetchHistoricalDataForTimestampByCoordinates(
            lat=latitude,
            lon=longitude,
            dt=dt
        ).json()

    def getStatisticalWeatherAggregatedYearlyFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedYearlyByCoordinates(
            lat=latitude,
            lon=longitude
        ).json()

    def getStatisticalWeatherAggregatedYearlyFromCityName(
        self,
        cityName: str,
        countryCode: Optional[str] = None
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedYearlyByCityName(
            cityName=cityName,
            countryCode=countryCode
        ).json()

    def getStatisticalWeatherAggregatedYearlyByCityId(
        self,
        cityId: int
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedYearlyByCityId(
            cityId=cityId
        ).json()

    def getStatisticalWeatherAggregatedMonthlyFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        month:int
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedMonthlyByCoordinates(
            lat=latitude,
            lon=longitude,
            month=month
        ).json()

    def getStatisticalWeatherAggregatedMonthlyFromCityName(
        self,
        cityName: str,
        month:int,
        countryCode: str = "US",
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedMonthlyByCityName(
            cityName=cityName,
            countryCode=countryCode,
            month=month
        ).json()

    def getStatisticalWeatherAggregatedMonthlyByCityId(
        self,
        cityId: int,
        month:int
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedMonthlyByCityId(
            cityId=cityId,
            month=month
        ).json()

    def getStatisticalWeatherAggregatedDailyFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        month:int,
        day:int
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedDailyByCoordinates(
            lat=latitude,
            lon=longitude,
            month=month,
            day=day
        ).json()

    def getStatisticalWeatherAggregatedDailyFromCityName(
        self,
        cityName: str,
        month: int,
        day: int,
        countryCode: str = "US",
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedDailyByCityName(
            cityName=cityName,
            countryCode=countryCode,
            month=month,
            day=day
        ).json()

    def getStatisticalWeatherAggregatedDailyByCityId(
        self,
        cityId: int,
        month:int,
        day:int
    ) -> Any:
        return self._context.fetchStatisticalWeatherDataAggregatedDailyByCityId(
            cityId=cityId,
            month=month,
            day=day
        ).json()

    def getAccumulatedTemperatureFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        start:float,
        end:float,
        threshold:int
    ) -> Any:
        return self._context.fetchAccumulatedTemperatureByCoordinates(
            lat=latitude,
            lon=longitude,
            start=start,
            end=end,
            threshold=threshold
        ).json()

    def getAccumulatedTemperatureFromCityName(
        self,
        cityName: str,
        start:float,
        end:float,
        threshold:int,
        countryCode: str = "US",
    ) -> Any:
        return self._context.fetchAccumulatedTemperatureByCityName(
            cityName=cityName,
            countryCode=countryCode,
            start=start,
            end=end,
            threshold=threshold
        ).json()

    def getAccumulatedTemperatureByCityId(
        self,
        cityId: int,
        start:float,
        end:float,
        threshold:int
    ) -> Any:
        return self._context.fetchAccumulatedTemperatureByCityId(
            cityId=cityId,
            start=start,
            end=end,
            threshold=threshold
        ).json()

    def getAccumulatedPrecipitationFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        start:float,
        end:float,
        threshold:int
    ) -> Any:
        return self._context.fetchAccumulatedPrecipitationByCoordinates(
            lat=latitude,
            lon=longitude,
            start=start,
            end=end,
            threshold=threshold
        ).json()

    def getAccumulatedPrecipitationFromCityName(
        self,
        cityName: str,
        start:float,
        end:float,
        threshold:int,
        countryCode: str = "US",
    ) -> Any:
        return self._context.fetchAccumulatedPrecipitationByCityName(
            cityName=cityName,
            countryCode=countryCode,
            start=start,
            end=end,
            threshold=threshold
        ).json()

    def getAccumulatedPrecipitationByCityId(
        self,
        cityId: int,
        start:float,
        end:float,
        threshold:int
    ) -> Any:
        return self._context.fetchAccumulatedPrecipitationByCityId(
            cityId=cityId,
            start=start,
            end=end,
            threshold=threshold
        ).json()

    def getAirPollutionCurrentDataFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float
    ) -> Any:
        return self._context.fetchCurrentAirPollutionByCoordinates(
            lat=latitude,
            lon=longitude
        ).json()

    def getAirPollutionForecastDataFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float
    ) -> Any:
        return self._context.fetchForecastAirPollutionByCoordinates(
            lat=latitude,
            lon=longitude
        ).json()

    def getAirPollutionHistoricalDataFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float
    ) -> Any:
        return self._context.fetchHistoricalAirPollutionByCoordinates(
            lat=latitude,
            lon=longitude
        ).json()

    def getCoordinatesByLocationName(
        self,
        cityName: str,
        countryCode: str,
        stateCode: Optional[str] = None,
        limitBy: Optional[int] = None
    ) -> Dict[Any, Any]:
        return self._context.fetchCoordinatesByName(
            cityName=cityName,
            stateCode=stateCode,
            countryCode=countryCode,
            limit=limitBy
        ).json()

    def getCoordinatesByZipCode(
        self,
        zipCode: int,
        countryCode: str
    ) -> Dict[Any, Any]:
        return self._context.fetchCoordinatesByZip(
            zipOrPostalCode=zipCode,
            countryCode=countryCode
        ).json()

    def getCoordinatesByPostalCode(
        self,
        postalCode: int,
        countryCode: str
    ) -> Dict[Any, Any]:
        return self._context.fetchCoordinatesByZip(
            zipOrPostalCode=postalCode,
            countryCode=countryCode
        ).json()
    
    def getNameOfLocationUsingLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float,
        limit: Optional[int] = None
    ) -> List[Dict[Any, Any]]:
        return self._context.fetchLocation(
            lat=latitude,
            lon=longitude,
            limit=limit
        ).json()
