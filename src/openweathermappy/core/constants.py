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
    CNT = "cnt"
    APPID = "appid"
    LIMIT = "limit"
    ZIP = "zip"
    Q = "q"
    TYPE = "type"
    START = "start"
    END = "end"
    UNITS = "units"
    LANG = "lang"
    ID = "id"
    EXCLUDE="exclude"
    DT = "dt"
    MONTH="month"
    DAY="day"
    THRESHOLD = "threshold"
