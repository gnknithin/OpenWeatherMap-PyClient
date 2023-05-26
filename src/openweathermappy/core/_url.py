class Resource:
    BASE_URL = "https://api.openweathermap.org"
    BASE_PRO_URL = "https://pro.openweathermap.org"
    BASE_HISTORY_URL = "https://history.openweathermap.org"
    GEOCODING_TYPE = "geo"
    DATA_TYPE = "data"


class Versions:
    VERSION_1_0 = "1.0"
    VERSION_2_5 = "2.5"
    VERSION_3_0 = "3.0"


class SubResource:
    ONECALL = "onecall"
    TIMEMACHINE = "timemachine"
    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    ACCUMULATED_TEMPERATURE = "accumulated_temperature"
    ACCUMULATED_PRECIPITATION = "accumulated_precipitation"
    FORCAST = "forecast"
    HISTORY = "history"
    AIR_POLLUTION = "air_pollution"
    AGGRIGATED = "aggregated"
    CITY = "city"
    HOURLY = "hourly"
    CLIMATE = "climate"
    DAILY = "daily"
    DIRECT = "direct"
    ZIP = "zip"
    REVERSE = "reverse"
    WEATHER = "weather"

class OpenWeatherMapURL:

    ONECALL_3_0_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_3_0,
            "/",
            SubResource.ONECALL
        ]
    )

    ONECALL_3_0_HISTORICAL_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_3_0,
            "/",
            SubResource.ONECALL,
            "/",
            SubResource.TIMEMACHINE
        ]
    )

    FORCAST_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.FORCAST
        ]
    )

    FORCAST_HOURLY_URL = "".join(
        [
            Resource.BASE_PRO_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.FORCAST,
            "/",
            SubResource.HOURLY
        ]
    )

    FORCAST_DAILY_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.FORCAST,
            "/",
            SubResource.DAILY
        ]
    )

    FORCAST_CLIMATE_URL = "".join(
        [
            Resource.BASE_PRO_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.FORCAST,
            "/",
            SubResource.CLIMATE
        ]
    )

    HISTORY_CITY_URL = "".join(
        [
            Resource.BASE_HISTORY_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.HISTORY,
            "/",
            SubResource.CITY
        ]
    )

    HISTORY_TIMESTAMP_URL = "".join(
        [
            Resource.BASE_HISTORY_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_3_0,
            "/",
            SubResource.HISTORY,
            "/",
            SubResource.TIMEMACHINE
        ]
    )

    STATISTICAL_AGGRIGATE_YEARLY_URL = "".join(
        [
            Resource.BASE_HISTORY_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.AGGRIGATED,
            "/",
            SubResource.YEAR
        ]
    )

    STATISTICAL_AGGRIGATE_MONTH_URL = "".join(
        [
            Resource.BASE_HISTORY_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.AGGRIGATED,
            "/",
            SubResource.MONTH
        ]
    )

    STATISTICAL_AGGRIGATE_DAILY_URL = "".join(
        [
            Resource.BASE_HISTORY_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.AGGRIGATED,
            "/",
            SubResource.DAY
        ]
    )

    ACCUMULATED_TEMPERATURE_URL = "".join(
        [
            Resource.BASE_HISTORY_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.HISTORY,
            "/",
            SubResource.ACCUMULATED_TEMPERATURE
        ]
    )

    ACCUMULATED_PRECIPITATION_URL = "".join(
        [
            Resource.BASE_HISTORY_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.HISTORY,
            "/",
            SubResource.ACCUMULATED_PRECIPITATION
        ]
    )

    CURRENT_AIR_POLLUTION_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.AIR_POLLUTION
        ]
    )

    FORECAST_AIR_POLLUTION_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.FORCAST
        ]
    )

    HISTORICAL_AIR_POLLUTION_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.HISTORY
        ]
    )

    GEOCODING_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.GEOCODING_TYPE,
            "/",
            Versions.VERSION_1_0
        ]
    )
    
    WEATHER_URL = "".join(
        [
            Resource.BASE_URL,
            "/",
            Resource.DATA_TYPE,
            "/",
            Versions.VERSION_2_5,
            "/",
            SubResource.WEATHER
        ]
    )

class GeocodingAPI:
    COORDINATES_BY_LOCATION_NAME_URL = "".join(
        [OpenWeatherMapURL.GEOCODING_URL, "/", SubResource.DIRECT]
    )
    COORDINATES_BY_ZIPCODE_OR_POSTCODE_URL = "".join(
        [OpenWeatherMapURL.GEOCODING_URL, "/", SubResource.ZIP]
    )
    REVERSE_GEOCODING_URL = "".join(
        [OpenWeatherMapURL.GEOCODING_URL, "/", SubResource.REVERSE]
    )
