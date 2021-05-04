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

```python
# PYTHON EXAMPLE
import requests

headers = {'Authorization': 'Bearer <auth_token>'}
params = { 'song_name': 'Runaway', 'artist': 'Kanye West' }

response = requests.get('<base_url>/api/songs', params=params, headers=headers)
response.raise_for_status()

print(response.json())
```

---

```
GET /api/votes
```

Returns list of all songs with the votes for each song. <br>

__Authentication:__ Bearer token for user account.

| Parameter         | Value                                                             |
| :---------------- | :-----------------------------------------------------------------|
| *votes*           | Filter by number of votes                                         |
| *sort*            | Sort the results. Acceptable values: asc, desc. Default: asc      |
| *song_name*       | Filter by the name of the song                                    |
| *artist*          | Filter by artist name                                             |
| *genre*           | Filter by genre. Acceptable values: Rock, HipHop, Metal, Pop, RnB |

<br>

```python
# PYTHON EXAMPLE
import requests

headers = {'Authorization': 'Bearer <auth_token>'}
params = { 'song_name': 'Runaway', 'artist': 'Kanye West' }

response = requests.get('<base_url>/api/votes', params=params, headers=headers)
response.raise_for_status()

print(response.json())
```

---

```
GET /api/votes/top/<count>
```

Returns list of first <count> songs with the votes for each song. <br>

__Authentication:__ Bearer token for user account.

| Parameter         | Value                                                             |
| :---------------- | :-----------------------------------------------------------------|
| *votes*           | Filter by number of votes                                         |
| *sort*            | Sort the results. Acceptable values: asc, desc. Default: asc      |
| *song_name*       | Filter by the name of the song                                    |
| *artist*          | Filter by artist name                                             |
| *genre*           | Filter by genre. Acceptable values: Rock, HipHop, Metal, Pop, RnB |

<br>

```python
# PYTHON EXAMPLE
import requests

headers = {'Authorization': 'Bearer <auth_token>'}
params = { 'song_name': 'Runaway', 'artist': 'Kanye West' }

response = requests.get('<base_url>/api/votes/top/5', params=params, headers=headers)
response.raise_for_status()

print(response.json())
```

---

###### STATUS CODES

| Status code       | Explanation          |
| :---------------- | :------------------- |
| *200..299*        | Successful request   |
| *403*             | Missing auth token   |
| *405*             | Invalid auth token   |
| *420*             | Bad Parameter        |
| *421*             | Bad parameter value  |
| *430*             | Unprocessable entity |


## POST Endpoints
- `/api/user_import` - Adds a user to db.users table

## Folder content
* __api_getter.py__
    - Consists of all API __GET__ endpoints.
* __api_post.py__
    - Consists of all API __POST__ endpoints.
