from abc import ABC
from typing import Any, Dict, List, Optional

import requests

from ._url import GeocodingAPI, OpenWeatherMapURL
from .constants import ParameterConstants


class BaseManager(ABC):
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def _prepare_request_params(self,) -> Dict[Any, Any]:
        _params: Dict[Any, Any] = dict()
        _params[ParameterConstants.APPID] = self._api_key
        return _params


class ContextManager(BaseManager):
    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)
    
    def fetchWeatherOneCallAPI(
            self,
            lat: float,
            lon: float,
            exclude:List[str],
            units: Optional[str],
            language: Optional[str]
        ):
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.EXCLUDE] = exclude
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG]= language
        return requests.get(
            url=OpenWeatherMapURL.ONECALL_3_0_URL,
            params=_prepared_params
        )

    def fetchHistoricalWeatherOneCallAPI(
            self,
            lat: float,
            lon: float,
            exclude:List[str],
            units: Optional[str],
            language: Optional[str]
        ):
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.EXCLUDE] = exclude
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG]= language
        return requests.get(
            url=OpenWeatherMapURL.ONECALL_3_0_HISTORICAL_URL,
            params=_prepared_params
        )

    def fetchCurrentWeatherByCoordinates(
        self,
        lat: float,
        lon: float,
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.WEATHER_URL,
            params=_prepared_params
        )

    def fetchCurrentWeatherByCityName(
        self,
        cityName: str,
        stateCode: Optional[str],
        countryCode: Optional[str],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if stateCode:
            queryLocation.append(stateCode)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.WEATHER_URL,
            params=_prepared_params
        )

    def fetchCurrentWeatherByCityId(
        self,
        cityId: int,
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.WEATHER_URL,
            params=_prepared_params
        )

    def fetchCurrentWeatherByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(str(zipCode))
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ZIP] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.WEATHER_URL,
            params=_prepared_params
        )

    def fetchHourlyForcastByCoordinates(
        self,
        lat: float,
        lon: float,
        cnt:Optional[int],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_HOURLY_URL,
            params=_prepared_params
        )

    def fetchHourlyForcastByCityName(
        self,
        cityName: str,
        stateCode: Optional[str],
        countryCode: Optional[str],
        cnt: Optional[int],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if stateCode:
            queryLocation.append(stateCode)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_HOURLY_URL,
            params=_prepared_params
        )

    def fetchHourlyForcastByCityId(
        self,
        cityId: int,
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_HOURLY_URL,
            params=_prepared_params
        )

    def fetchHourlyForcastByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(str(zipCode))
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ZIP] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_HOURLY_URL,
            params=_prepared_params
        )

    def fetchDailyForcastByCoordinates(
        self,
        lat: float,
        lon: float,
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_DAILY_URL,
            params=_prepared_params
        )

    def fetchDailyForcastByCityName(
        self,
        cityName: str,
        stateCode: Optional[str],
        countryCode: Optional[str],
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if stateCode:
            queryLocation.append(stateCode)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_DAILY_URL,
            params=_prepared_params
        )

    def fetchDailyForcastByCityId(
        self,
        cityId: int,
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_DAILY_URL,
            params=_prepared_params
        )

    def fetchDailyForcastByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str],
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(str(zipCode))
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ZIP] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_DAILY_URL,
            params=_prepared_params
        )

    def fetchClimateForcastByCoordinates(
        self,
        lat: float,
        lon: float,
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_CLIMATE_URL,
            params=_prepared_params
        )

    def fetchClimateForcastByCityName(
        self,
        cityName: str,
        countryCode: Optional[str],
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_CLIMATE_URL,
            params=_prepared_params
        )

    def fetchClimateForcastByCityId(
        self,
        cityId: int,
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_CLIMATE_URL,
            params=_prepared_params
        )

    def fetchClimateForcastByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str],
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(str(zipCode))
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ZIP] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_CLIMATE_URL,
            params=_prepared_params
        )

    def fetchWeatherForcastByCoordinates(
        self,
        lat: float,
        lon: float,
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_URL,
            params=_prepared_params
        )

    def fetchWeatherForcastByCityName(
        self,
        cityName: str,
        stateCode: Optional[str],
        countryCode: Optional[str],
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if stateCode:
            queryLocation.append(stateCode)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_URL,
            params=_prepared_params
        )

    def fetchWeatherForcastByCityId(
        self,
        cityId: int,
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_URL,
            params=_prepared_params
        )

    def fetchWeatherForcastByZipCode(
        self,
        zipCode: int,
        countryCode: Optional[str],
        cnt: Optional[int],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(str(zipCode))
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ZIP] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.CNT] = cnt
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.FORCAST_URL,
            params=_prepared_params
        )

    def fetchHourlyHistoricalDataByCoordinates(
        self,
        lat: float,
        lon: float,
        start: Optional[float],
        end: Optional[float],
        cnt:Optional[int],
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.TYPE] = "hour"
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.CNT] = cnt
        return requests.get(
            url=OpenWeatherMapURL.HISTORY_CITY_URL,
            params=_prepared_params
        )

    def fetchHourlyHistoricalDataByCityName(
        self,
        cityName: str,
        countryCode: Optional[str],
        cnt: Optional[int],
        start: Optional[float],
        end: Optional[float]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.TYPE] = "hour"
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.CNT] = cnt
        return requests.get(
            url=OpenWeatherMapURL.HISTORY_CITY_URL,
            params=_prepared_params
        )

    def fetchHourlyHistoryDataByCityId(
        self,
        cityId: int,
        start: Optional[float],
        end: Optional[float],
        cnt: Optional[int]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.TYPE] = "hour"
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.CNT] = cnt
        return requests.get(
            url=OpenWeatherMapURL.HISTORY_CITY_URL,
            params=_prepared_params
        )

    def fetchHistoricalDataForTimestampByCoordinates(
        self,
        lat: float,
        lon: float,
        dt: float
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.DT] = dt
        return requests.get(
            url=OpenWeatherMapURL.HISTORY_TIMESTAMP_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedYearlyByCoordinates(
        self,
        lat: float,
        lon: float
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_YEARLY_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedYearlyByCityName(
        self,
        cityName: str,
        countryCode: Optional[str],
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_YEARLY_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedYearlyByCityId(
        self,
        cityId: int,
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_YEARLY_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedMonthlyByCoordinates(
        self,
        lat: float,
        lon: float,
        month:int
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.MONTH] = month
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_MONTH_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedMonthlyByCityName(
        self,
        cityName: str,
        countryCode: Optional[str],
        month:int
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.MONTH] = month
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_MONTH_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedMonthlyByCityId(
        self,
        cityId: int,
        month: int
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.MONTH] = month
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_MONTH_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedDailyByCoordinates(
        self,
        lat: float,
        lon: float,
        month:int,
        day:int
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.MONTH] = month
        _prepared_params[ParameterConstants.DAY] = day
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_DAILY_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedDailyByCityName(
        self,
        cityName: str,
        countryCode: Optional[str],
        month:int,
        day:int
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.MONTH] = month
        _prepared_params[ParameterConstants.DAY] = day
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_DAILY_URL,
            params=_prepared_params
        )

    def fetchStatisticalWeatherDataAggregatedDailyByCityId(
        self,
        cityId: int,
        month:int,
        day:int
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.MONTH] = month
        _prepared_params[ParameterConstants.DAY] = day
        return requests.get(
            url=OpenWeatherMapURL.STATISTICAL_AGGRIGATE_DAILY_URL,
            params=_prepared_params
        )

    def fetchAccumulatedTemperatureByCoordinates(
        self,
        lat: float,
        lon: float,
        start: float,
        end: float,
        threshold:int
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.THRESHOLD] = threshold
        return requests.get(
            url=OpenWeatherMapURL.ACCUMULATED_TEMPERATURE_URL,
            params=_prepared_params
        )

    def fetchAccumulatedTemperatureByCityName(
        self,
        cityName: str,
        countryCode: Optional[str],
        start: float,
        end: float,
        threshold:int
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.THRESHOLD] = threshold
        return requests.get(
            url=OpenWeatherMapURL.ACCUMULATED_TEMPERATURE_URL,
            params=_prepared_params
        )

    def fetchAccumulatedTemperatureByCityId(
        self,
        cityId: int,
        start: float,
        end: float,
        threshold:int
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.THRESHOLD] = threshold
        return requests.get(
            url=OpenWeatherMapURL.ACCUMULATED_TEMPERATURE_URL,
            params=_prepared_params
        )

    def fetchAccumulatedPrecipitationByCoordinates(
        self,
        lat: float,
        lon: float,
        start: float,
        end: float,
        threshold:int
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.THRESHOLD] = threshold
        return requests.get(
            url=OpenWeatherMapURL.ACCUMULATED_PRECIPITATION_URL,
            params=_prepared_params
        )

    def fetchAccumulatedPrecipitationByCityName(
        self,
        cityName: str,
        countryCode: Optional[str],
        start: float,
        end: float,
        threshold:int
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.THRESHOLD] = threshold
        return requests.get(
            url=OpenWeatherMapURL.ACCUMULATED_PRECIPITATION_URL,
            params=_prepared_params
        )

    def fetchAccumulatedPrecipitationByCityId(
        self,
        cityId: int,
        start: float,
        end: float,
        threshold:int
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.START] = start
        _prepared_params[ParameterConstants.END] = end
        _prepared_params[ParameterConstants.THRESHOLD] = threshold
        return requests.get(
            url=OpenWeatherMapURL.ACCUMULATED_PRECIPITATION_URL,
            params=_prepared_params
        )

    def fetchCurrentAirPollutionByCoordinates(
        self,
        lat: float,
        lon: float
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        return requests.get(
            url=OpenWeatherMapURL.CURRENT_AIR_POLLUTION_URL,
            params=_prepared_params
        )

    def fetchForecastAirPollutionByCoordinates(
        self,
        lat: float,
        lon: float
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        return requests.get(
            url=OpenWeatherMapURL.FORECAST_AIR_POLLUTION_URL,
            params=_prepared_params
        )

    def fetchHistoricalAirPollutionByCoordinates(
        self,
        lat: float,
        lon: float
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        return requests.get(
            url=OpenWeatherMapURL.HISTORICAL_AIR_POLLUTION_URL,
            params=_prepared_params
        )

    def fetchLocation(
        self,
        lat: float,
        lon: float,
        limit: Optional[int]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.LIMIT] = limit
        return requests.get(
            url=GeocodingAPI.REVERSE_GEOCODING_URL,
            params=_prepared_params
        )

    def fetchCoordinatesByZip(
        self,
        zipOrPostalCode: int,
        countryCode: str
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ZIP] = f"{zipOrPostalCode},{countryCode}"
        return requests.get(
            url=GeocodingAPI.COORDINATES_BY_ZIPCODE_OR_POSTCODE_URL,
            params=_prepared_params
        )

    def fetchCoordinatesByName(
        self,
        cityName: str,
        stateCode: Optional[str],
        countryCode: Optional[str],
        limit: Optional[int]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(cityName)
        if stateCode:
            queryLocation.append(stateCode)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.Q] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.LIMIT] = limit
        return requests.get(
            url=GeocodingAPI.COORDINATES_BY_LOCATION_NAME_URL,
            params=_prepared_params
        )
