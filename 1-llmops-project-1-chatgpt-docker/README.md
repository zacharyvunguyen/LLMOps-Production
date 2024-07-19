# FastAPI OpenAI Integration

This repository contains a FastAPI application that integrates with the OpenAI API to provide a simple chatbot interface and some basic endpoints.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Endpoints](#endpoints)
- [Running the Application](#running-the-application)
- [License](#license)

## Installation

1. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Create a `config.py` file in the root of the project and add your OpenAI API key and assistant ID:
```python
# config.py

api_key = "your_openai_api_key"
assistant_id = "your_assistant_id"
```

## Endpoints

### `GET /`
Returns a welcome message.
- **Response:**
    ```json
    {
      "message": "Hello World"
    }
    ```

### `GET /home`
Returns a home page welcome message.
- **Response:**
    ```json
    {
      "message": "Welcome to my home page"
    }
    ```

### `POST /chat`
Echoes the input text.
- **Request Body:**
    ```json
    {
      "text": "your input text"
    }
    ```
- **Response:**
    ```json
    {
      "message": "your input text"
    }
    ```

### `POST /response`
Generates a response using the OpenAI assistant based on the input text.
- **Request Body:**
    ```json
    {
      "text": "your input text"
    }
    ```
- **Response:**
    ```json
    {
      "message_content": "generated response from OpenAI assistant"
    }
    ```

## Running the Application

1. Ensure you have the required configurations in `config.py`.
2. Run the application using Uvicorn:
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 80
    ```
   For development, use the `--reload` option to enable auto-reload on code changes:
    ```sh
    uvicorn main:app --reload
    ```

The application will be accessible at `http://127.0.0.1:8000` when using the default `--reload` configuration.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` now includes instructions for running the application in development mode with the `--reload` option.