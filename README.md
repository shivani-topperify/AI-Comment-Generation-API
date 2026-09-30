# AI Comment Generation API

A FastAPI-based Generative AI application that generates natural, context-aware social media comment drafts using Google's Gemini API and stores generated comments in a SQLite database.

---

## 1. Project Overview

The **AI Comment Generation API** is a REST API designed to automate the process of drafting relevant and natural comments for social media posts.

The application accepts information about a social media post, including the platform, community, title, and content. It uses Google's Gemini API to generate a suitable comment based on the provided context.

Generated comments are stored in a SQLite database using SQLAlchemy and can be retrieved or deleted through API endpoints.

The API is documented and tested using FastAPI's built-in Swagger UI.

---

## 2. Problem Statement

Writing relevant and natural comments for social media posts can be time-consuming.

Users may understand a topic but still find it difficult to formulate a response that:

* Matches the platform
* Matches the conversation
* Adds useful information
* Sounds natural
* Does not sound like an advertisement

This project aims to automate the comment drafting process using Generative AI while preserving the context of the original social media post.

---

## 3. Objectives

The main objectives of the project are to:

1. Accept a social media post as input.
2. Understand the platform and community context.
3. Generate a relevant comment using Generative AI.
4. Return the generated comment through a REST API.
5. Store generated comments in a database.
6. Retrieve previously generated comments.
7. Retrieve an individual comment using its ID.
8. Delete stored comments.
9. Validate incomplete or incorrect requests.
10. Handle requests for non-existing comments appropriately.

---

## 4. Features

### AI Comment Generation

Generates natural-language comment drafts using Google's Gemini API.

### Platform Awareness

The API accepts a platform such as:

* Reddit
* LinkedIn
* Other supported social platforms

The platform information is included in the prompt so that the generated response can be appropriate for the requested context.

### Community Context

The API accepts a community or context such as:

* UPSC
* careers
* technology
* programming

### Context-Aware Prompt Engineering

The application creates a structured prompt containing:

* Platform
* Community
* Post title
* Post content
* Comment-writing instructions

### Database Storage

Generated comments are stored using:

* SQLite
* SQLAlchemy

### Comment History

Previously generated comments can be retrieved through the API.

### Individual Comment Retrieval

A specific stored comment can be retrieved using its database ID.

### Comment Deletion

Stored comments can be deleted using their ID.

### Input Validation

FastAPI and Pydantic validate required request fields.

For example, if `post_content` is missing, the API returns a `422 Unprocessable Content` response.

### Error Handling

The API returns a `404 Not Found` response when a requested comment does not exist.

---

## 5. Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Generative AI

* Google Gemini API
* Google GenAI Python SDK

### Database

* SQLite
* SQLAlchemy

### Validation

* Pydantic

### API Documentation and Testing

* FastAPI Swagger UI
* OpenAPI

### Development Tools

* Visual Studio Code
* Python Virtual Environment
* Git
* GitHub

---

## 6. Project Structure

```text
Reddit-Comment-API/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── prompts.py
│   ├── llm.py
│   ├── models.py
│   └── database.py
│
├── comments.db
├── .gitignore
├── requirements.txt
├── README.md
└── AI_Comment_Generation_API_Architecture (2).puml
```

The `.env` file is used locally for the Gemini API key and is excluded from Git using `.gitignore`.

---

## 7. File Responsibilities

### `main.py`

Initializes the FastAPI application and registers the API routes.

### `routes.py`

Contains the API endpoints for:

* Generating comments
* Retrieving all comments
* Retrieving an individual comment
* Deleting comments

### `schemas.py`

Defines request and response structures using Pydantic.

### `prompts.py`

Contains the prompt-building logic used to provide structured instructions to the Gemini model.

### `llm.py`

Handles communication with the Google Gemini API.

### `models.py`

Defines the SQLAlchemy database model for stored comments.

### `database.py`

Configures the SQLite database and SQLAlchemy database session.

---

## 8. API Endpoints

| Method | Endpoint                 | Description                      |
| ------ | ------------------------ | -------------------------------- |
| POST   | `/generate-comment`      | Generate and store an AI comment |
| GET    | `/comments`              | Retrieve all stored comments     |
| GET    | `/comments/{comment_id}` | Retrieve a specific comment      |
| DELETE | `/comments/{comment_id}` | Delete a stored comment          |
| GET    | `/`                      | Home endpoint                    |

---

## 9. Generate Comment

### POST `/generate-comment`

Generates an AI comment based on the supplied social media post.

### Request

```json
{
  "platform": "reddit",
  "post_title": "How to stay consistent with UPSC preparation?",
  "post_content": "I keep losing motivation while preparing. What should I do?",
  "community": "UPSC"
}
```

### Response

```json
{
  "platform": "reddit",
  "comment": "Honestly, stop relying on motivation. It’s a trap. UPSC is too long of a journey for motivation to last. You need to build discipline and routine instead."
}
```

The exact generated comment may vary because it is generated dynamically by Gemini.

---

## 10. Get All Comments

### GET `/comments`

Returns previously generated comments stored in the database.

### Example Response

```json
[
  {
    "id": 2,
    "platform": "reddit",
    "community": "UPSC",
    "post_title": "How to prepare for UPSC?",
    "post_content": "What is the best strategy for starting UPSC preparation?",
    "generated_comment": "Honestly, the best way to start is by thoroughly reading the syllabus and analyzing the last few years of PYQs.",
    "created_at": "2026-08-13T07:12:05.392297"
  }
]
```

---

## 11. Get Individual Comment

### GET `/comments/{comment_id}`

Retrieves a specific generated comment using its database ID.

### Example

```text
GET /comments/2
```

### Successful Response

```json
{
  "platform": "reddit",
  "community": "UPSC",
  "post_content": "What is the best strategy for starting UPSC preparation?",
  "created_at": "2026-08-13T07:12:05.392297",
  "id": 2,
  "post_title": "How to prepare for UPSC?",
  "generated_comment": "Honestly, the best way to start is by thoroughly reading the syllabus and analyzing the last few years of PYQs."
}
```

### Comment Not Found

If the requested ID does not exist:

```json
{
  "detail": "Comment not found"
}
```

---

## 12. Delete Comment

### DELETE `/comments/{comment_id}`

Deletes a stored comment using its database ID.

### Example

```text
DELETE /comments/2
```

### Successful Response

```json
{
  "message": "Comment deleted successfully",
  "id": 2
}
```

### Comment Not Found

If the requested ID does not exist:

```json
{
  "detail": "Comment not found"
}
```

---

## 13. API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

The OpenAPI specification is available at:

```text
http://127.0.0.1:8000/openapi.json
```

Swagger UI can be used to test the API endpoints without requiring a separate frontend application.

---

## 14. How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/shivani-topperify/AI-Comment-Generation-API.git
```

### Step 2: Open the Project

```bash
cd AI-Comment-Generation-API
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure the Gemini API Key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file should remain local and must not be committed to GitHub.

### Step 7: Start the API

```bash
python -m uvicorn app.main:app
```

The API will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 15. Example Workflow

A typical workflow is:

### Step 1 — User provides a social media post

```text
Platform: Reddit

Community: UPSC

Title:
How to stay consistent with UPSC preparation?

Content:
I keep losing motivation while preparing. What should I do?
```

### Step 2 — Application creates a structured prompt

The application combines the platform, community, title, content, and comment-writing instructions.

### Step 3 — Prompt is sent to Gemini

The Gemini API generates a context-aware comment.

### Step 4 — API returns the generated comment

The generated comment is returned in the API response.

### Step 5 — Comment is stored

The generated comment and associated post information are stored in SQLite.

### Step 6 — User can manage stored comments

The user can:

* Retrieve all comments
* Retrieve an individual comment
* Delete a comment

---

## 16. Prompt Engineering

The application uses a structured prompt instead of sending only the original post content to the AI model.

The prompt includes:

* Platform
* Community
* Post title
* Post content

The model is also given instructions such as:

* Write one natural comment.
* Do not sound like an advertisement.
* Do not mention that the response was generated by AI.
* Keep the comment relevant to the post.
* Match the platform's conversational style.
* Return only the comment.

This approach provides the model with additional context when generating the response.

---

## 17. Database

The project uses SQLite for persistent storage of generated comments.

SQLAlchemy is used as the ORM for interacting with the database.

Each stored comment contains information such as:

* ID
* Platform
* Community
* Post title
* Post content
* Generated comment
* Created time

### Example Database Record

```json
{
  "id": 3,
  "platform": "linkedin",
  "community": "careers",
  "post_title": "Importance of consistency in career growth",
  "post_content": "How can someone consistently improve their professional skills?",
  "generated_comment": "For me, the key is shifting from massive sessions to daily micro-habits.",
  "created_at": "2026-08-13T07:13:05"
}
```

---

## 18. Validation Testing

The API was tested with an incomplete request.

For example, `post_content` was intentionally omitted:

```json
{
  "platform": "reddit",
  "post_title": "Test post",
  "community": "UPSC"
}
```

The API returned:

```text
422 Unprocessable Content
```

Response:

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "body",
        "post_content"
      ],
      "msg": "Field required"
    }
  ]
}
```

This confirms that required request fields are validated by FastAPI and Pydantic.

---

## 19. API Testing Results

The implemented API endpoints were tested through FastAPI Swagger UI.

| Test                     | Expected Result | Actual Result |
| ------------------------ | --------------: | ------------: |
| POST `/generate-comment` |             200 |           200 |
| GET `/comments`          |             200 |           200 |
| GET `/comments/{id}`     |             200 |           200 |
| DELETE `/comments/{id}`  |             200 |           200 |
| Missing required field   |             422 |           422 |

The tests confirmed that comment generation, database retrieval, deletion, and request validation are functioning correctly.

---

## 20. Error Handling Testing

The API was also designed to handle requests for comments that do not exist.

### Example

```text
GET /comments/9999
```

If the comment does not exist, the API returns:

```json
{
  "detail": "Comment not found"
}
```

Similarly:

```text
DELETE /comments/9999
```

returns:

```json
{
  "detail": "Comment not found"
}
```

This prevents invalid database operations from being silently accepted.

---

## 21. Platform Testing

The API accepts platform information as part of the request.

### Reddit

Example:

```text
Platform: reddit
Community: UPSC
```

The generated response is instructed to follow a conversational Reddit-style approach.

### LinkedIn

Example:

```text
Platform: linkedin
Community: careers
```

The platform information is provided to the prompt so the generated response can be adapted to the requested professional context.

---

## 22. Current Project Status

The following components have been implemented and tested:

* Python project setup
* Virtual environment
* FastAPI
* Uvicorn
* Gemini integration
* Google GenAI SDK
* Prompt engineering
* AI comment generation
* SQLite database
* SQLAlchemy
* Comment storage
* Get all comments
* Get individual comment
* Delete comment
* Request validation
* Error handling
* Reddit testing
* LinkedIn testing
* Multiple input testing
* Swagger API documentation
* OpenAPI documentation
* API endpoint testing

---

## 23. Future Improvements

Possible future improvements include:

### Frontend

Create a simple web interface where users can paste a social media post and generate a comment through a graphical interface.

### More Platform Support

Extend the system to support additional social media platforms and platform-specific response styles.

### Multiple Comment Suggestions

Generate multiple comment options, such as:

1. Professional
2. Casual
3. Short
4. Detailed

### Authentication

Add user authentication so each user can maintain a separate comment history.

### Deployment

Deploy the API to a cloud platform so that it can be accessed remotely.

### Social Media Integration

Integrate with official social media APIs where permitted, allowing generated drafts to be used within supported workflows.

---

## 24. Conclusion

The **AI Comment Generation API** demonstrates how Generative AI can be integrated with a REST API to automate social media comment drafting.

The system accepts contextual information about a social media post, generates a relevant comment using Google's Gemini API, returns the generated result through FastAPI, and stores the generated comment in a SQLite database.

The project combines:

```text
REST API
+
Generative AI
+
Prompt Engineering
+
Database
+
Validation
+
API Testing
```

to create a functional AI-powered comment generation system.

---

## 25. Author

**Shivani Alagesan**

AI Comment Generation API
Final Year Project

GitHub Repository:

https://github.com/shivani-topperify/AI-Comment-Generation-API
