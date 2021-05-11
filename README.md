# 2021_RJukebox

Simple project which demonstrates __Web API__ implementation using *Flask framework* <br>
The idea is followed by a web site, where users can add and vote for their favorite song.

Users can register through the web site to get their own *access token*, which in turn will be used as authentication for an API. <br>

Once the song is entered through the website - token of the user which added the song will be automatically linked to the song itself, meaning that only mentioned user will have an authorization to delete or change the song, while anyone can vote for that song.

## Get Started

Entry point for starting flask server is [application.sh](https://github.com/MATF-Computer-Networks-Projects/2021_RJukebox/blob/main/application.sh) which will:
* install all required python modules, which are located in [requirements.txt](https://github.com/MATF-Computer-Networks-Projects/2021_RJukebox/blob/main/requirements.txt)
* initialize all the necessary environment variables
* Start flask server - currently localhost
* Run the entry point: [application.py](https://github.com/MATF-Computer-Networks-Projects/2021_RJukebox/blob/main/application.py)

__Note:__ Don't forget to CD to the repository folder before starting flask server.

Once the flask server started - you can use the website and API through Postman, Thunder Client (VSCode extension), or prefered programming language.

__Note:__ You will need MySQL server running on your machine.

## API

You can use an API endpoints to add / modify / delete / get informations about songs, and vote for your favorite song. <br>

For the information about API endpoints visit [API Documentation](https://github.com/MATF-Computer-Networks-Projects/2021_RJukebox/blob/main/api/README.md)

## Required Environment Variables

Environment variables can be set through creating local `.env` file:

```
USER=your_db_username
PASSWORD=your_db_password
SECRET_KEY=secret_key
```

`SECRET_KEY` will be used by application to encode the token and passwords.

## Logging

Application will create log file in the format `applicationLogs_Year_Month_Day_Hour_Minute.log` which can be used for debugging.
* Each time you start an application, new log file will be created
* Log files older than 3 days will be automatically deleted on application startup
* Same logs are also sent on standard output

Logging configuration is located in [logger_config.ini](https://github.com/MATF-Computer-Networks-Projects/2021_RJukebox/blob/main/configurations/logger_config.ini) file.

## Contributors

* [Nikola Damjanovic](https://github.com/damiapp)
* [Milos Nikolic](https://github.com/somislav)
* [Luka Kumburovic](https://github.com/SpotRZ)
