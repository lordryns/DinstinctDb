
---

# DistinctDb API Documentation

Welcome to the DistinctDb API documentation. DistinctDb is a database API designed for easy data storage using JSON files. Below, you'll find details on how to interact with the API.

## Base URL

For demonstration purposes, the base URL of the API is:

```
https://distinctdb.onrender.com/
```

## Endpoints

### Create Database

- **URL**: `/create_db/`
- **Method**: `POST`
- **Description**: Creates a new JSON database.
- **Request Body**:
  ```json
  {
    "name": "Item Name",
    "description": "Item Description"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Response in text.",
    "key": "the-database-key", 
    "success": true
  }
  ```
  **or just use the DistinctDb site to create a database easily at** [distinctdb](https://distinctdb.vercel.app)

### Create Item

- **URL**: `/add_data/`
- **Method**: `POST`
- **Description**: Creates a new (key / value) item in the database.
- **Request Body**:
  ```json
  {
    "db_key": "your-db-key", 
    "title": "the key", 
    "value": "The value to assign",
    "data_type": "str | int | bool | float"
  }
  ```

- **Response**:
  ```json
  {
    "message": "The API response", 
    "success": true
  }
  ```

### Get Items

- **URL**: `/get_data/{key}`
- **Method**: `GET`
- **Description**: Retrieves all data from the database associated with the provided key.
- **Response**:
  ```json
  {
    "message": "Success message", 
    "key": "your-api-key",
    "data": {}, 
    "success": true
  }
  ```

## Contact

For questions, feedback, or support, you can reach out to the project owner:

- Twitter: [@lordryns](https://twitter.com/lordryns)

---

