# Django Bench - Async REST API Benchmark Application

A Django application with async REST API using ADRF (Async Django REST Framework), Knox authentication, PostgreSQL, uvicorn, and uvloop. This application provides CRUD endpoints for Posts and Comments with nested routing.

## Features

- **Async API**: Built with ADRF for high-performance async operations
- **Token Authentication**: Secure authentication using django-rest-knox
- **PostgreSQL Database**: Production-ready database backend
- **uvicorn + uvloop**: High-performance ASGI server with optimized event loop
- **Custom User Model**: Extensible user authentication
- **Nested Routes**: RESTful API with comments nested under posts
- **Seed Data**: Command to generate test data for benchmarking

## Project Structure

```
django-bench/
├── backend/                 # Main Django project
│   ├── settings.py         # Django settings
│   ├── urls.py            # URL configuration
│   └── asgi.py            # ASGI configuration with uvloop
├── users/                  # Custom user app
│   ├── models.py          # Custom User model
│   └── management/
│       └── commands/
│           ├── create_token.py  # Token generation command
│           └── seed.py          # Database seeding command
├── posts/                  # Posts app
│   ├── models.py          # Post model
│   ├── serializers.py     # Post serializers
│   ├── views.py           # Async Post viewsets
│   └── urls.py            # Post URL routing
└── comments/              # Comments app
    ├── models.py          # Comment model
    ├── serializers.py     # Comment serializers
    └── views.py           # Async Comment viewsets
```

## Dependencies

- Python 3.14
- PostgreSQL 17
- Poetry (for dependency management)

## Installation

1. **Clone the repository** (if applicable)

2. **Install dependencies with Poetry**:

   ```bash
   cd /path/to/django-bench
   poetry install
   ```

3. **Set up PostgreSQL database**:

   ```bash
   # Create PostgreSQL database
   createdb django_bench

   # Or using psql
   psql -c "CREATE DATABASE django_bench;"
   ```

4. **Configure database** (optional):

   Set environment variables for database connection:

   ```bash
   export DB_NAME=django_bench
   export DB_USER=postgres
   export DB_PASSWORD=postgres
   export DB_HOST=localhost
   export DB_PORT=5432
   ```

5. **Run migrations**:

   ```bash
   poetry run python manage.py migrate
   ```

6. **Seed the database** (optional but recommended):

   ```bash
   poetry run python manage.py seed
   ```

   This will create:

   - A test user (username: `testuser`, password: `testpass123`)
   - 1000 sample posts
   - An authentication token for API access

## Running the Server

Start the development server with uvicorn:

```bash
poetry run uvicorn backend.asgi:application --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

All endpoints require authentication. Include the token in the `Authorization` header:

```
Authorization: Token <your-token-here>
```

### Posts

- **List all posts**: `GET /api/posts/`
- **Create a post**: `POST /api/posts/`
- **Get a post**: `GET /api/posts/{id}/`
- **Update a post**: `PUT /api/posts/{id}/`
- **Partial update**: `PATCH /api/posts/{id}/`
- **Delete a post**: `DELETE /api/posts/{id}/`

### Comments (Nested under Posts)

- **List comments for a post**: `GET /api/posts/{post_id}/comments/`
- **Create a comment**: `POST /api/posts/{post_id}/comments/`
- **Get a comment**: `GET /api/posts/{post_id}/comments/{id}/`
- **Update a comment**: `PUT /api/posts/{post_id}/comments/{id}/`
- **Partial update**: `PATCH /api/posts/{post_id}/comments/{id}/`
- **Delete a comment**: `DELETE /api/posts/{post_id}/comments/{id}/`

## Management Commands

### Create Authentication Token

Create a token for an existing user:

```bash
poetry run python manage.py create_token <username>
```

### Seed Database

Generate test data for benchmarking:

Options:

- `--posts N`: Number of posts to create (default: 1000)

Example:

```bash
poetry run python manage.py seed --posts 5000
```

## Usage Examples

### Using curl

1. **Get authentication token** (if you ran the seed command):

   ```bash
   # The token is displayed after running the seed command
   export TOKEN="your-token-here"
   ```

2. **List posts**:

   ```bash
   curl -H "Authorization: Token $TOKEN" http://localhost:8000/api/posts/
   ```

3. **Create a post**:

   ```bash
   curl -X POST \
     -H "Authorization: Token $TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"text": "My new post"}' \
     http://localhost:8000/api/posts/
   ```

4. **Get a specific post**:

   ```bash
   curl -H "Authorization: Token $TOKEN" http://localhost:8000/api/posts/1/
   ```

5. **Create a comment on a post**:

   ```bash
   curl -X POST \
     -H "Authorization: Token $TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"text": "Great post!"}' \
     http://localhost:8000/api/posts/1/comments/
   ```

6. **List comments for a post**:
   ```bash
   curl -H "Authorization: Token $TOKEN" http://localhost:8000/api/posts/1/comments/
   ```

## Libs

- **Djang**: Web framework
- **Django REST Framework**: REST API toolkit
- **ADRF**: Async Django REST Framework
- **django-rest-kno**: Token authentication
- **uvicorn**: ASGI server
- **uvloop**: Fast event loop implementation
- **PostgreSQL**: Database (via psycopg2-binary)
- **Faker**: Test data generation

## Development

### Create a superuser

```bash
poetry run python manage.py createsuperuser
```

### Access Django Admin

Visit `http://localhost:8000/admin/` and log in with your superuser credentials.

### Run tests

```bash
poetry run python manage.py test
```

## Performance Considerations

- **Async Views**: All API endpoints use async viewsets for better concurrency
- **uvloop**: Provides 2-4x performance improvement over standard asyncio
- **Database Indexing**: Models include indexes on frequently queried fields
- **Select Related**: Queries use `select_related()` to minimize database hits
