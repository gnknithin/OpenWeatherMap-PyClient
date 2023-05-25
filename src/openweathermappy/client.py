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
            exclude:List[str]
        ):
        return self._context.fetchOneCallAPI(
            lat=latitude,
            lon=longitude,
            exclude=exclude
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

    def getCoordinatesByZipCode(
        self,
        zipCode: str,
        countryCode: str
    ) -> Dict[Any, Any]:
        return self._context.fetchCoordinatesByZip(
            zipOrPostalCode=zipCode,
            countryCode=countryCode
        ).json()

    def getCoordinatesByPostalCode(
        self,
        postalCode: str,
        countryCode: str
    ) -> Dict[Any, Any]:
        return self._context.fetchCoordinatesByZip(
            zipOrPostalCode=postalCode,
            countryCode=countryCode
        ).json()

    def getCoordinatesByLocationName(
        self,
        cityName: str,
        countryCode: str,
        stateCodeOnlyForUS: Optional[str] = None,
        limitBy: Optional[int] = None
    ) -> Dict[Any, Any]:
        return self._context.fetchCoordinatesByName(
            cityName=cityName,
            stateCode=stateCodeOnlyForUS,
            countryCode=countryCode,
            limit=limitBy
        ).json()

    def getCurrentWeatherDataByZipCode(
        self,
        zipCode: str,
        countryCode: str
    ) -> Dict[Any, Any]:
        return self._context.fetchCurrentWeatherByZipCode(
            zipCode=zipCode,
            countryCode=countryCode,
            mode=None,
            units=None,
            language=None
        ).json()

    def getCurrentWeatherDataByCityId(
        self,
        cityId: str
    ) -> Dict[Any, Any]:
        return self._context.fetchCurrentWeatherByCityId(
            cityId=cityId,
            mode=None,
            units=None,
            language=None
        ).json()

    def getCurrentWeatherDataByCityName(
        self,
        cityName: str,
        stateCode: Optional[str] = None,
        countryCode: Optional[str] = None
    ) -> Dict[Any, Any]:
        return self._context.fetchCurrentWeatherByCityName(
            cityName=cityName,
            stateCode=stateCode,
            countryCode=countryCode,
            mode=None,
            units=None,
            language=None
        ).json()

    def getCurrentWeatherDataFromLatitudeAndLongitude(
        self,
        latitude: float,
        longitude: float
    ) -> Dict[Any, Any]:
        return self._context.fetchCurrentWeatherByCoordinates(
            lat=latitude,
            lon=longitude,
            mode=None,
            units=None,
            language=None
        ).json()
