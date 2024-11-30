# RUDRAM_PROJECT

This is a Django-based API project to manage **User Profiles** and **Posts**. The API provides various endpoints to perform CRUD operations on User Profiles and Posts.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## Project Overview

Rudram Project is designed to manage **User Profiles** and **Posts**. The project exposes RESTful API endpoints for operations like creating, reading, updating, and deleting user profiles and posts.

## Technologies Used

- Python 3.11.2
- Django 5.1.3
- PostgreSQL
- Django REST Framework 3.15.2
- Swagger (API Documentation)

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Akshay78980/rudram-project.git
cd rudram-project
```

### 2. Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 3. Setup .env File

Create a .env file to store sensitive configuration variables.
  1. Copy the .env.example file to .env:
     
      ```bash
      cp .env.example .env
      ```
  2. Generate a Django SECRET_KEY using the following Python code:
      
      ```python
      
      from django.core.management.utils import get_random_secret_key
      print(get_random_secret_key())

      ```

  3. Add the generated SECRET_KEY to your .env file:
      ```arduino
      
      SECRET_KEY='your-generated-secret-key-here'

      ```
  4. Configure your database settings in .env:
     
      ```makefile
      DEBUG=True
      ALLOWED_HOSTS='127.0.0.1, localhost'
      
      DB_NAME='postgres_rudram_db'
      DB_USER='postgres_rudram_user'
      DB_PASSWORD='your-database-password'
      DB_PORT='5432'
      DB_HOST='localhost'
      ```

### 4. Apply Database Migrations

Apply the database migrations to set up the necessary tables:

```bash
python manage.py migrate
```

### 5. Run the Development Server
Now you can run the development server:

```bash
python manage.py runserver
```

Visit the following URLs in your browser or API client (like Postman) to interact with the API:
- **Profiles API**: `http://127.0.0.1:8000/api/profiles/`
- **Posts API**: `http://127.0.0.1:8000/api/posts/`

Ensure the server is running before accessing these endpoints.

## Configuration

Here are the environment variables you need to configure in your `.env` file:

- **SECRET_KEY**:  
  The secret key used for cryptographic signing. This is a crucial security feature for Django. Ensure this value is kept private and secure.

- **DEBUG**:  
  Set to `True` for development purposes and `False` for production.

- **ALLOWED_HOSTS**:  
  A comma-separated list of allowed hosts for your application. For example: `'127.0.0.1, localhost'`.

- **DB_NAME**:  
  The name of your PostgreSQL database.

- **DB_USER**:  
  The username for your PostgreSQL database.

- **DB_PASSWORD**:  
  The password for your PostgreSQL database.

- **DB_HOST**:  
  The host address of your PostgreSQL database. Typically set to `localhost` for local development.

- **DB_PORT**:  
  The port number for your PostgreSQL database. Default is usually `5432`.

Make sure to configure these variables correctly before running the application.

## API Documentation
The API exposes the following endpoints for managing User Profiles and Posts:

### UserProfile Endpoints

- **`GET /api/profiles`**:  Retrieve a list of user profiles.

- **`POST /api/profiles`**:  Create a new user profile.

- **`GET /api/profiles/{id}`**:  Retrieve a specific user profile.

- **`PUT /api/profiles/{id}`**:  Update an existing user profile.

- **`PATCH /api/profiles/{id}`**:  Partially update an existing user profile.

- **`DELETE /api/profiles/{id}`**:  Delete a user profile.


### Post Endpoints

- **`GET /api/posts`**:  Retrieve a list of posts.

- **`POST /api/posts`**:  Create a new post.

- **`GET /api/posts/{id}`**:  Retrieve a specific post.

- **`DELETE /api/posts/{id}`**:  DELETE /api/posts/{id}

For a full, interactive API documentation, visit [**SwaggerHub - RUDRAM_PROJECT_API_3.0**](https://app.swaggerhub.com/apis/PAKSHAYSUGATHAN/RUDRAM_PROJECT_API_3.0/1.0.0).


## Testing the API

You can test the API using the SwaggerHub mock server or use tools like Postman to send requests.

### Test the API with SwaggerHub
1. Visit the SwaggerHub mock server: [SwaggerHub Mock Server](https://virtserver.swaggerhub.com/PAKSHAYSUGATHAN/RUDRAM_PROJECT_API_3.0/1.0.0).
2. Use the provided mock API to test the requests.

Alternatively, you can test the real API by running the local server as mentioned above.

---


