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


## PATCH Endpoints

- Each endpoint that accepts PATCH requires `song_name`, `artist` and `update` parameters
- __Note:__ If you want to change more than one parameter with one request, use POST

| Parameter         | Value                                                             |
| :---------------- | :-----------------------------------------------------------------|
| *song_name*       | Song name for the song you wish to alter                          |
| *artist*          | Artist for the song you wish to alter                             |
| *update*          | New value for field. Field itself is specified by endpoint        |

---

```
PATCH /api/songs/name
```

Updates name of the song uniquely recognized by `song_name / artist` parameters with specified `update` parameter. <br>

__Authentication:__ Bearer token for user account.

---

```
PATCH /api/songs/artist
```

Updates artist of the song uniquely recognized by `song_name / artist` parameters with specified `update` parameter. <br>

__Authentication:__ Bearer token for user account.

---

```
PATCH /api/songs/genre
```

Updates genre of the song uniquely recognized by `song_name / artist` parameters with specified `update` parameter. <br>

__Authentication:__ Bearer token for user account.

---

```
PATCH /api/songs/link
```

Updates youtube link of the song uniquely recognized by `song_name / artist` parameters with specified `update` parameter. <br>

__Authentication:__ Bearer token for user account.

---

###### STATUS CODES

| Status code       | Explanation          |
| :---------------- | :------------------- |
| *200..299*        | Successful request   |
| *403*             | Missing auth token   |
| *405*             | Invalid auth token   |
| *406*             | Bad Parameter        |
| *430*             | Unprocessable entity |


```python
# PYTHON EXAMPLE
import requests

headers = {'Authorization': 'Bearer <auth_token>'}
params = { 'song_name': 'Runaway', 'artist': 'Kanye West', 'update': 'HipHop' }

response = requests.patch('<base_url>/api/songs/genre', params=params, headers=headers)
response.raise_for_status()

print(response.json())
```


## POST Endpoints

```
POST /api/user_import
```

Imports a user into db. <br>

| Parameter         | Value                                                             |
| :---------------- | :-----------------------------------------------------------------|
| *name*            | User name for your account.                                       |
| *password*        | Password for your account.                                        |

<br>

```python
# PYTHON EXAMPLE
import requests

params = { 'Name': 'Nikola', 'password': 'sifra' }

response = requests.post('<base_url>/api/user_import', params=params)
response.raise_for_status()

print(response.json())
```

---

```
POST /api/add_song
```
__Authentication:__ Bearer token for user account.

Imports song into db. <br>

| Parameter         | Value                                                             |
| :---------------- | :-----------------------------------------------------------------|
| *song_name*       | Song name for the song being added.                               |
| *atist*           | Artist which has played the song.                                 |
| *genre*           | Genre of the song being added.                                    |
| *yt_link*         | YouTube link for the song.                                        |

<br>

```python
# PYTHON EXAMPLE
import requests

headers = {'Authorization': 'Bearer <auth_token>'}
params = { 'song_name': 'Runaway', 'artist': 'Kanye West', 'genre': 'HipHop', 'yt_link': 'https://www.youtube.com/...' }

response = requests.post('<base_url>/api/add_song', params=params, headers=headers)
response.raise_for_status()

print(response.json())
```

---


###### STATUS CODES

| Status code       | Explanation           |
| :---------------- | :-------------------  |
| *200..299*        | Successful request    |
| *300*             | Already exist warning |
| *401*             | Missing param value   |
| *403*             | Missing auth token    |
| *405*             | Invalid auth token    |
| *420*             | Bad Parameter         |
| *421*             | Bad parameter value   |
| *430*             | Unprocessable entity  |


## DELETE ENDPOINT

```
DELETE /api/songs
```
Deletes a song from db. <br>

| Parameter         | Value                                                             |
| :---------------- | :-----------------------------------------------------------------|
| *song_name*       | Song name for the song being deleted.                             |
| *atist*           | Artist which has played the song.                                 |

<br>

```python
# PYTHON EXAMPLE
import requests

headers = {'Authorization': 'Bearer <auth_token>'}
params = { 'song_name': 'Runaway', 'artist': 'Kanye West'}

response = requests.delete('<base_url>/api/songs', params=params, headers=headers)
response.raise_for_status()

print(response.json())

```


###### STATUS CODES

| Status code       | Explanation           |
| :---------------- | :-------------------  |
| *405*             | Bad song name value   |
| *430*             | Unprocessable entity  |



## Folder content
* __api_getter.py__
    - Consists of all API __GET__ endpoints.
* __api_post.py__
    - Consists of all API __POST__ endpoints.
* __api_patch.py__
    - Consists of all API __PATCH__ endpoints.
