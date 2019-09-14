# RESTful API Matcha

#### Note
All data should be sent to server in JSON file.

Schemas are in backend/db/models.py

## Endpoints

http://localhost:5000/

### Users

```
GET     /api/users -> get all users
POST     /api/users -> add a user
GET     /api/users/<user_id> -> get one user by id
```

Example for adding a user:
```
{
    "user_name": "myName"
}

```