class ClientEnvironmentVariable:
    OPENWEATHERMAP_API_KEY = "OPENWEATHERMAP_API_KEY"


class ErrorMessage:
    INITIALIZATION_FAILURE = f"{ClientEnvironmentVariable.OPENWEATHERMAP_API_KEY} environment variable not found, initialization failure!"


class ParameterConstants:
    LAT = "lat"
    LON = "lon"
    APPID = "appid"
    LIMIT = "limit"
    ZIP = "zip"
    Q = "q"
    MODE = "mode"
    UNITS = "units"
    LANG = "lang"
    ID = "id"


class Resource:
    BASE_URL = "https://api.openweathermap.org"
    GEOCODING_TYPE = "geo"
    DATA_TYPE = "data"


class SubResource:
    DIRECT = "direct"
    ZIP = "zip"
    REVERSE = "reverse"
    WEATHER = "weather"


class Versions:
    VERSION_1_0 = "1.0"
    VERSION_2_5 = "2.5"
    VERSION_3_0 = "3.0"


class OpenWeatherMapURL:
    GEOCODING_URL = f"{Resource.BASE_URL}/{Resource.GEOCODING_TYPE}/{Versions.VERSION_1_0}"
    WEATHER_URL = f"{Resource.BASE_URL}/{Resource.DATA_TYPE}/{Versions.VERSION_2_5}/{SubResource.WEATHER}"


class GeocodingAPI:
    COORDINATES_BY_LOCATION_NAME_URL = f"{OpenWeatherMapURL.GEOCODING_URL}/{SubResource.DIRECT}"
    COORDINATES_BY_ZIPCODE_OR_POSTCODE_URL = f"{OpenWeatherMapURL.GEOCODING_URL}/{SubResource.ZIP}"
    REVERSE_GEOCODING_URL = f"{OpenWeatherMapURL.GEOCODING_URL}/{SubResource.REVERSE}"
