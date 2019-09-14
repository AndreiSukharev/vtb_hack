# RESTful API Matcha

#### Note
All data should be sent to server in JSON file.

Schemas are in backend/db/models.py

## Endpoints

 
 ### Sign In
```
POST     /api/signin -> Sign In
```

These keys are required to sign in a user:
```
login, password
```
Example for POST:
```
{
    "login": "test1",
    "password": "123Wertyq"
}
 ```

 ### Log out
```
DELETE     /api/logout
```

### Users

```
GET     /api/users -> get all users
GET     /api/users/<user_id> -> get one user by id
```

Response for getting one user:
```
{
    "user_id": 4,
    "login": "test",
    "email": "mr.andrey.sd@gmail.com",
   
}

```

### Chats

```
GET     /api/chats  -> get chats of the doc
GET    /api/chats/<chat_id>  -> get the certain chat with messages
```
Example GET response
```
[
    {
        "chat_name": "kek",
        "chat_id": 3
    },
    {
        "chat_name": "cheburek",
        "chat_id": 5
    }
]
```

Example GET <chat_id>  response
```
{
    "messages": [
        {
            "creation_date": "2019-08-07 15:34:07",
            "text": "asdad",
            "author": "test1"
        },
        {
            "creation_date": "2019-08-07 15:34:11",
            "text": "asdd",
            "author": "test2"
        }
    ],
    "partner_id": 2
}
```

### Socket

```
/api/socket -> connect to socket
    
```
Events

on:

```
'connect' -> connected to socket
'receive_message(message)' -> get message from server to another user
'notification(message)' -> notificate about message, fake, history, likes, dislikes

```

emit:

```
'connect_logged_user(user_id)' -> after sign in send user_id
```

```
'join(chat_id)' -> send chat_id to join the chat
```

```
'message(message)' -> send message 
{
    "text": "Hello",
    "chat_id": "1", -> get this from url
    "author": "YoYo", -> login of user
    "creation_date": "2019-09-02T09:25:07.561Z", -> new Date(),
    "partner_id": '2'
}
```

```
'manage_notification(data)' -> send notification 
{
    "author": "YoYo", -> login of user
    "partner_id": "2", for whom notification
    "type": "history" or "like" or "dislike" or "fake"
}
```


