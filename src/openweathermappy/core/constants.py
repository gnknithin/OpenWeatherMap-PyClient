class ClientEnvironmentVariable:
    OPENWEATHERMAP_API_KEY = "OPENWEATHERMAP_API_KEY"


class ErrorMessage:
    INITIALIZATION_FAILURE = "".join(
        [
            ClientEnvironmentVariable.OPENWEATHERMAP_API_KEY,
            " environment variable not found, initialization failure!"
        ]
    )


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
    EXCLUDE="exclude"
