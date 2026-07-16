# To-Do CRUD API Specification

## Overview
This project is a backend API that manages a to-do list. It implements the four standard CRUD operations (Create, Read, Update, Delete) using strictly in-memory data storage (no database).

## Technology Stack Options
Choose ONE of the following lanes to build the API:
- **Python Lane**: Python 3.10+ using FastAPI (Swagger UI is built-in).
- **JavaScript Lane**: Node.js using Express (Requires `swagger-ui-express` and `openapi.json` for Swagger UI).

## Data Model
- Tasks are represented as objects with three fields:
  - `id` (integer)
  - `title` (string)
  - `done` (boolean)
- The in-memory list should be pre-filled with 3 example tasks upon server start.

## API Endpoints

### General Endpoints
- **`GET /`**
  - **Description**: API metadata.
  - **Response (200 OK)**: `{"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}`
- **`GET /health`**
  - **Description**: Health check endpoint.
  - **Response (200 OK)**: `{"status": "ok"}`

### Task CRUD Endpoints
- **`GET /tasks`**
  - **Description**: Retrieve all tasks.
  - **Response (200 OK)**: A JSON array of all task objects.

- **`GET /tasks/:id`** (or `{id}`)
  - **Description**: Retrieve a specific task by ID.
  - **Response (200 OK)**: The matching task object.
  - **Error (404 Not Found)**: If no task matches the ID, return `{"error": "Task [id] not found"}`.

- **`POST /tasks`**
  - **Description**: Create a new task.
  - **Request Body**: JSON object containing at least a `title` (e.g., `{"title": "Buy milk"}`).
  - **Behavior**: Auto-increment the `id`, set `done` to `false` by default, and append to the list.
  - **Response (201 Created)**: The newly created task object.
  - **Error (400 Bad Request)**: If the `title` is missing or empty, return a JSON error message.

- **`PUT /tasks/:id`** (or `{id}`)
  - **Description**: Update an existing task.
  - **Request Body**: JSON object with `title` and/or `done`.
  - **Behavior**: Update the fields of the target task.
  - **Response (200 OK)**: The fully updated task object.
  - **Error (400 Bad Request)**: If the request body is empty or invalid.
  - **Error (404 Not Found)**: If no task matches the ID.

- **`DELETE /tasks/:id`** (or `{id}`)
  - **Description**: Delete a specific task.
  - **Behavior**: Remove the task from the in-memory list.
  - **Response (204 No Content)**: Empty response body on success.
  - **Error (404 Not Found)**: If no task matches the ID.

## Interactive Documentation
- **Swagger UI** must be available at the `/docs` endpoint, fully documenting the API and allowing requests via a "Try it out" interface.

## Strict Requirements
1. **In-Memory Only**: Do not use a database or file storage. Data must reset when the server restarts.
2. **Proper Status Codes**: You must strictly use 200, 201, 204, 400, and 404 exactly as specified above.
3. **Validation**: All POST and PUT endpoints must validate the incoming JSON body.
4. **JSON Responses**: All responses, including errors, must be in valid JSON format.
