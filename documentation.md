
# Flask-api



## Indices

* [Default](#default)

  * [/register](#1-register)
  * [/login](#2-login)
  * [/movies](#3-movies)
  * [/addMovie](#4-addmovie)
  * [/addEpisode](#5-addepisode)


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



### 3. /movies



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



### 4. /addMovie



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
| name | Hunter x Hunter |  |



### 5. /addEpisode



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
| preview_url |  | image perview of episode |



---
[Back to top](#flask-api)
> Made with &#9829; by [thedevsaddam](https://github.com/thedevsaddam) | Generated at: 2020-05-30 10:59:18 by [docgen](https://github.com/thedevsaddam/docgen)
