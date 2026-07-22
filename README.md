# Build Your First CRUD API (Node.js & Express)

## Project Description
This is a small backend API that manages a to-do list, built as part of the "Build your first CRUD API" assignment. The project has been switched to **JavaScript (Node.js & Express)**.

It implements the four standard CRUD operations (Create, Read, Update, Delete) using Express. All task data is stored in-memory (no database), meaning the data resets whenever the server restarts.

## Project Structure
```text
first-crud-api/
├── index.js                  # Core Express application file containing all routing and logic
├── openapi.json              # OpenAPI specification for the API endpoints
├── package.json              # NPM package configurations and dependency listings
├── package-lock.json         # Lockfile for NPM dependencies
├── .gitignore                # Ignored files (node_modules, venv, pycache, etc.)
├── swagger-screenshot.png    # Screenshot of the Swagger UI
└── README.md                 # Project documentation
```

## Setup and Run Instructions

To install dependencies and start the server locally, run the following commands in your terminal:

```bash
# Install dependencies
npm install

# Start the server (configured to run node index.js)
npm start
```

*The server will start on `http://localhost:3000`.*

---

## Endpoints

### `GET /`

Returns metadata about the API.

**Response**

```json
{
  "name": "Task API",
  "version": "1.0",
  "endpoints": ["/tasks"]
}
```

**Example**

```bash
curl http://localhost:3000/
```

### `GET /health`

Health check endpoint.

**Response**

```json
{
  "status": "ok"
}
```

**Example**

```bash
curl http://localhost:3000/health
```

### `GET /tasks`

Returns all tasks. Optional query parameters filter the list (the part after `?` — filters, not addresses).

| Query | Example | Effect |
|-------|---------|--------|
| `done` | `?done=true` | Only finished tasks |
| `done` | `?done=false` | Only open tasks |
| `search` | `?search=milk` | Title contains the word (case-insensitive) |

Filters can be combined: `?done=false&search=book`

**Response**

```json
[
  { "id": 1, "title": "Buy groceries", "done": false },
  { "id": 2, "title": "Walk the dog", "done": true },
  { "id": 3, "title": "Read a book", "done": false }
]
```

**Example**

```bash
curl http://localhost:3000/tasks
curl "http://localhost:3000/tasks?done=true"
curl "http://localhost:3000/tasks?search=milk"
```

### `GET /stats`

Returns computed counts for the current task list.

**Response**

```json
{ "total": 7, "done": 3, "open": 4 }
```

**Example**

```bash
curl http://localhost:3000/stats
```

### `POST /reset`

Restores the three seed example tasks. Useful for demos and testing.

**Response (200)**

```json
[
  { "id": 1, "title": "Buy groceries", "done": false },
  { "id": 2, "title": "Walk the dog", "done": true },
  { "id": 3, "title": "Read a book", "done": false }
]
```

**Example**

```bash
curl -X POST http://localhost:3000/reset
```

### `GET /tasks/:id`

Returns a single task by id.

**Response (200)**

```json
{ "id": 1, "title": "Buy groceries", "done": false }
```

**Response (404)**

```json
{ "error": "Task 99 not found" }
```

**Example**

```bash
curl http://localhost:3000/tasks/1
curl http://localhost:3000/tasks/99
```

### `POST /tasks`

Creates a new task.

**Request body**

```json
{ "title": "Buy milk" }
```

**Response (201)**

```json
{ "id": 4, "title": "Buy milk", "done": false }
```

**Response (400)**

```json
{ "error": "title is required and cannot be empty" }
```

**Example**

```bash
curl -X POST http://localhost:3000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk"}'
```

### `PUT /tasks/:id`

Updates a task's `title` and/or `done`. Send one or both fields; omitted fields stay unchanged.

**Request body**

```json
{ "title": "Buy oat milk", "done": true }
```

**Response (200)**

```json
{ "id": 1, "title": "Buy oat milk", "done": true }
```

**Response (400)**

```json
{ "error": "request body must include title and/or done" }
```

**Response (404)**

```json
{ "error": "Task 99 not found" }
```

**Example**

```bash
curl -X PUT http://localhost:3000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```

### `DELETE /tasks/:id`

Deletes a task.

**Response (204)**

Empty body — success, nothing to return.

**Response (404)**

```json
{ "error": "Task 99 not found" }
```

**Example**

```bash
curl -X DELETE http://localhost:3000/tasks/1
```

---

## Interactive Documentation (Swagger UI)

Express serves the interactive Swagger API documentation automatically using `swagger-ui-express` and `openapi.json`. Once the server is running, visit:

👉 **`http://localhost:3000/docs`**

![Swagger UI](swagger-ui.png)
