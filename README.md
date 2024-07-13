Note! this is just a demo documentation! 

## This documentation is not valid or accurate!
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
- **Description**: Creates a new json database.
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
        "success": "true or false"
    }

**or just use the DistinctDb site to create a database easily at** [distinctdb](https://distinctdb.vercel.app)
 


### Create item

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
    "message": "The api response", 
    "success": "true or false"
  }
  ```


### Get Items

- **URL**: `/get_data`
- **Method**: `GET`
- **Description**: Returns all the data in the database.
- **Response**:
  ```json
  {
    "message": "Item deleted successfully"
  }
  ```
- **Error Responses**:
  - Status Code: `404 Not Found`
    ```json
    {
      "detail": "Item not found"
    }
    ```

## Usage

To interact with the DistinctDb API, use tools like `curl`, Postman, or any HTTP client library in your preferred programming language. Simply replace `{item_id}` and `{base_url}` with the appropriate values for your API setup.

## Contact

For questions, feedback, or support, you can reach out to the project owner:

- Twitter (X): [@lordryns](https://twitter.com/lordryns)

---

