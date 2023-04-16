[![Coverage Status](https://coveralls.io/repos/github/gnknithin/OpenWeatherMap-PyClient/badge.svg?branch=main)](https://coveralls.io/github/gnknithin/OpenWeatherMap-PyClient?branch=main)
# OpenWeatherMap-PyClient
A simple wrapper around [OpenWeatherMap APIs](https://openweathermap.org/api) using Python, allow users to interact OpenWeatherMap platform to retrieve weather information

## Get Started

### Installation

You can install **OpenWeatherMap-PyClient** as :

    pip install git+https://github.com/gnknithin/OpenWeatherMap-PyClient.git@main

After the installation, add ``OPENWEATHERMAP_API_KEY`` to the environment variable

### API Key
As OpenWeatherMap API's require authorization to process our requests, please proceed to [OpenWeatherMap API Section](https://home.openweathermap.org/api_keys) to **create** / **retrieve** you API Key

For windows users, run the following commands in a command prompt:

    setx OPENWEATHERMAP_API_KEY "YOUR-OPENWEATHERMAP-API-KEY"

For UNIX or LINUX or MAC users, add the line to ``~/.bashrc`` or ``~/.zshrc`` using terminal:
    
    export OPENWEATHERMAP_API_KEY=YOUR-OPENWEATHERMAP-API-KEY


Project Links
=============
- Issues: https://github.com/gnknithin/OpenWeatherMap-PyClient/issues

License
=======

MIT licensed. See the bundled [LICENSE](https://github.com/gnknithin/OpenWeatherMap-PyClient/blob/main/LICENSE) file for more details.