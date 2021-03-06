
# Flask-api



## Indices

* [Default](#default)

  * [/register](#1-register)
  * [/login](#2-login)
  * [/refresh](#3-refresh)
  * [/movies](#4-movies)
  * [/addMovie](#5-addmovie)
  * [/addEpisode](#6-addepisode)


--------


## Default



### 1. /register



***Endpoint:***

```bash
Method: POST
Type: URLENCODED
URL: http://localhost/register
```



***Body:***


| Key | Value | Description |
| --- | ------|-------------|
| username |  | username |
| password |  | password |



### 2. /login



***Endpoint:***

```bash
Method: POST
Type: URLENCODED
URL: http://localhost/login
```



***Body:***


| Key | Value | Description |
| --- | ------|-------------|
| username |  | username |
| password |  | password |


### 3. /refresh



***Endpoint:***

```bash
Method: POST
Type: 
URL: http://localhost/refresh
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer <refresh_token from /login> |  |




### 4. /movies



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://localhost/movies
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer <access_token from /login> |  |



### 5. /addMovie



***Endpoint:***

```bash
Method: POST
Type: URLENCODED
URL: http://localhost/addMovie
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer <access_token from /login> |  |



***Body:***


| Key | Value | Description |
| --- | ------|-------------|
| name | | movie name |



### 6. /addEpisode



***Endpoint:***

```bash
Method: POST
Type: URLENCODED
URL: http://localhost/addEpisode
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer <access_token from /login> |  |



***Body:***


| Key | Value | Description |
| --- | ------|-------------|
| id |  | id of movie in json file |
| title |  | title of episode |
| url |  | url of episode |
| preview_url |  | image preview of episode |



---
[Back to top](#flask-api)
> Made with &#9829; by [thedevsaddam](https://github.com/thedevsaddam) | Generated at: 2020-05-30 10:59:18 by [docgen](https://github.com/thedevsaddam/docgen)
- [Post man collection](https://www.postman.com/collections/d19a3c51400b06a0fbda)
