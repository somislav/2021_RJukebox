## User Class

```
__init__(self,name,password)
```

User class for breaking down the user logic. <br>

| Parameter         | Value                                     |   
| :---------------- | :--------------------------------------   |
| *name*            | String for user name.                     |
| *password*        | String for password which is hashed after.|

<br>
---

```
validate_user(self) -> bool:
```

Validating user for existense. <br>

| Return Value      | Meaning                                   |   
| :---------------- | :--------------------------------------   |
| *True*            | User does not exist.                      |
| *False*           | User does exist.                          |

<br>

---

```
input_user(self) -> bool:
```

Adding user into db. <br>

| Return Value      | Meaning                                   |   
| :---------------- | :--------------------------------------   |
| *True*            | User added.                               |
| *False*           | User not added.                           |

<br>
---

```
get_encoded_token(self) -> str
```

Getter for Auth token. <br>

| Return Value      | Meaning                                   |   
| :---------------- | :--------------------------------------   |
| *None*            | Error occured.                            |
| *token*           | Token which was encoded wiht jwt.         |

<br>

---

## Song class

```
__init__(self, artist, genre, song_name, yt_link, token)
```

Song class for breaking down the song logic. <br>

| Parameter         | Value                                |
| :---------------- | :------------------------------------|
| *song_name*       | Song name for the song.              |
| *atist*           | Artist which has played the song.    |
| *genre*           | Genre of the song.                   |
| *yt_link*         | YouTube link for the song.           |
| *token*           | User token for Authentication.       |

<br>

---

```
check_if_song_exists(self) -> bool
```

Validating user for existense. <br>

| Return Value      | Meaning                                   |   
| :---------------- | :--------------------------------------   |
| *True*            | Song does not exist.                      |
| *False*           | Song does exist.                          |

<br>

---

```
input_song(self) -> bool:
```

Adding user into db. <br>

| Return Value      | Meaning                                   |   
| :---------------- | :--------------------------------------   |
| *True*            | Song added.                               |
| *False*           | Song not added.                           |

<br>