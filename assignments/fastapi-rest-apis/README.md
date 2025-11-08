# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small RESTful API using the FastAPI framework. Students will design endpoints, use Pydantic models for validation, return JSON responses with appropriate status codes, and run the app locally with Uvicorn.

**Skills practiced:** HTTP methods and status codes, request/response JSON, input validation with Pydantic, routing, basic async handlers, running a development server.

## 📝 Tasks

### 🛠️ Build the API

#### Description
Implement a small API for managing a collection of resources (for example, "items"). The API should support creating, listing, retrieving and deleting items. Use Pydantic models for request validation and clear JSON responses.

#### Requirements
Completed project should:

- Provide at least the following endpoints:
  - `GET /items` — return a list of items
  - `GET /items/{item_id}` — return a single item or 404
  - `POST /items` — create a new item from a JSON body (validate with Pydantic)
  - `DELETE /items/{item_id}` — remove an item or return 404
- Use Pydantic `BaseModel` for request/response schemas
- Return appropriate HTTP status codes (200, 201, 204, 404, 400 when applicable)
- Include basic error handling using `HTTPException`
- Provide clear instructions to run the app with Uvicorn (development mode)

### 🛠️ Add optional enhancements

#### Description
Add features that make the API more robust, user-friendly, or production-like. Pick at least one enhancement to implement.

#### Requirements
Completed project may include one or more of the following enhancements:

- Add `PUT` or `PATCH` to update items
- Add query parameters for filtering or pagination (`limit`, `skip`, `q`)
- Persist data to a simple SQLite database (SQLModel / SQLAlchemy) instead of in-memory storage
- Add basic authentication (API key or simple token) to protect write endpoints
- Add automated tests for main endpoints (pytest + httpx)
- Document the API with OpenAPI (FastAPI does this automatically) and include example requests

---

Starter code is included in `starter-code.py`. Update or extend it as needed. To run locally:

```bash
pip install -r requirements.txt
uvicorn starter-code:app --reload
```
