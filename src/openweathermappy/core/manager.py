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
    
    def fetchOneCallAPI(
            self,
            lat: float,
            lon: float,
            exclude:List[str]
        ):
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.EXCLUDE] = exclude
        return requests.get(
            url=OpenWeatherMapURL.ONECALL_3_0_URL,
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
        zipOrPostalCode: str,
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

    def fetchCurrentWeatherByZipCode(
        self,
        zipCode: str,
        countryCode: str,
        mode: Optional[str],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        queryLocation: List[Any] = list()
        queryLocation.append(zipCode)
        if countryCode:
            queryLocation.append(countryCode)
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ZIP] = ",".join(queryLocation)
        _prepared_params[ParameterConstants.MODE] = mode
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.WEATHER_URL,
            params=_prepared_params
        )

    def fetchCurrentWeatherByCityId(
        self,
        cityId: str,
        mode: Optional[str],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.ID] = cityId
        _prepared_params[ParameterConstants.MODE] = mode
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
        mode: Optional[str],
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
        _prepared_params[ParameterConstants.MODE] = mode
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.WEATHER_URL,
            params=_prepared_params
        )

    def fetchCurrentWeatherByCoordinates(
        self,
        lat: float,
        lon: float,
        mode: Optional[str],
        units: Optional[str],
        language: Optional[str]
    ) -> requests.Response:
        _prepared_params = self._prepare_request_params()
        _prepared_params[ParameterConstants.LAT] = lat
        _prepared_params[ParameterConstants.LON] = lon
        _prepared_params[ParameterConstants.MODE] = mode
        _prepared_params[ParameterConstants.UNITS] = units
        _prepared_params[ParameterConstants.LANG] = language
        return requests.get(
            url=OpenWeatherMapURL.WEATHER_URL,
            params=_prepared_params
        )
