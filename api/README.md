Folder with all API endpoints.<br>
Each API method is realized through flask `Blueprint` concept and should be kept in different file.<br>
Each API method __needs to start with /api/__<br>


## GET Endpoints

```
GET /api/songs
```

Returns list of all songs and respective info. <br>

__Authentication:__ Bearer token for user account.

| Parameter         | Value                                                             |
| :---------------- | :-----------------------------------------------------------------|
| *song_name*       | Filter by the name of the song                                    |
| *artist*          | Filter by artist name                                             |
| *genre*           | Filter by genre. Acceptable values: Rock, HipHop, Metal, Pop, RnB |
| *yt_link*         | Filter by youtube link, *include complete link*.                  |

<br>

| Return code       | Explanation          |
| :---------------- | :------------------- |
| *200..299*        | Successful request   |
| *420*             | Bad Parameter        |
| *430*             | Unprocessable entity |
| *403*             | Missing auth token   |
| *405*             | Invalid auth token   |

<br>

```python
# PYTHON EXAMPLE
import requests

headers = {'Authorization': 'Bearer <auth_token>'}
params = { 'song_name': 'Runaway', 'artist': 'Kanye West' }

response = requests.get('<base_url>/api/songs', params=params, headers=headers)
response.raise_for_status()

print(response.json())
```

## POST Endpoints
- `/api/user_import` - Adds a user to db.users table

## Folder content
* __api_getter.py__
    - Consists of all API __GET__ endpoints.
* __api_post.py__
    - Consists of all API __POST__ endpoints.
