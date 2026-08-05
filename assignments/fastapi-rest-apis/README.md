# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a small REST API with FastAPI and learn how routes, request validation, path parameters, query parameters, and response models work together. By the end, you will have a documented API for managing a simple resource in memory.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Descrição
Create the base FastAPI application and make sure the project starts with a working health check endpoint.

#### Requisitos
O programa concluído deve:

- Create a FastAPI app instance
- Expose a `GET /health` endpoint that returns a success message
- Run without errors using a standard ASGI server such as Uvicorn

### 🛠️ Build CRUD Endpoints for a Resource

#### Descrição
Implement endpoints to create, read, update, and delete a simple resource such as books, tasks, or courses using in-memory storage.

#### Requisitos
O programa concluído deve:

- Support `GET /items` to list all records
- Support `GET /items/{id}` to retrieve a single record
- Support `POST /items` to create a new record
- Support `PUT /items/{id}` or `PATCH /items/{id}` to update an existing record
- Support `DELETE /items/{id}` to remove a record

### 🛠️ Add Validation and Filtering

#### Descrição
Improve the API so it rejects invalid input and allows clients to narrow results with query parameters.

#### Requisitos
O programa concluído deve:

- Validate request bodies with Pydantic models
- Return a clear error when a record is not found
- Accept at least one query parameter for filtering or searching results
- Return structured JSON responses for success and failure cases
