\# AI Comment Generation API



An AI-powered REST API that generates natural, relevant social media comment drafts based on a user's post.



The system accepts a social media platform, post title, post content, and community/context. It uses Google's Gemini model to generate a suitable comment and stores the generated comment in a SQLite database.



\---



\## 1. Project Overview



People often come across posts on platforms such as Reddit or LinkedIn and want to respond but do not know what to write.



This project provides an AI-based solution that generates a natural and useful comment based on the context of the original post.



\### Basic workflow



User Post

↓

FastAPI

↓

Prompt Engineering

↓

Gemini AI

↓

Generated Comment

↓

SQLite Database



The generated comment can then be copied and posted by the user on the respective social media platform.



\---



\## 2. Problem Statement



Writing relevant and natural comments for social media posts can take time.



Users may understand a topic but struggle to formulate a suitable response that:



\- Matches the platform

\- Matches the conversation

\- Adds useful information

\- Sounds natural

\- Does not sound like an advertisement



This project aims to automate the comment drafting process using Generative AI.



\---



\## 3. Objective



The main objective is to develop an API that can:



1\. Accept a social media post as input.

2\. Understand the platform and community context.

3\. Generate a relevant comment using Generative AI.

4\. Return the generated comment through an API response.

5\. Store generated comments in a database.

6\. Allow users to retrieve previous comments.

7\. Allow users to delete stored comments.

8\. Validate incorrect or incomplete requests.



\---



\## 4. Features



\### AI Comment Generation



Generates natural comments using Google's Gemini API.



\### Platform Awareness



The API accepts different platforms such as:



\- Reddit

\- LinkedIn

\- Other social platforms



The generated response is instructed to match the platform's conversational style.



\### Community Context



The API can accept a community such as:



```text

UPSC

careers

technology

programming



Prompt Engineering



A structured prompt is created using:



Platform

Community

Post title

Post content

Comment-writing rules

Database Storage



Generated comments are stored using SQLite and SQLAlchemy.



Comment History



Previously generated comments can be retrieved using the API.



Delete Comments



Stored comments can be deleted using their ID.



Input Validation



FastAPI automatically validates required fields and returns a 422 response when required information is missing.



Error Handling



The API returns appropriate errors when a requested comment does not exist.



5\. Technology Stack

Backend

Python

FastAPI

Uvicorn

AI

Google Gemini API

Google GenAI Python SDK

Database

SQLite

SQLAlchemy

Validation

Pydantic

API Testing

FastAPI Swagger UI

OpenAPI

Development

Visual Studio Code

Python Virtual Environment

Git

6\. Project Structure

Reddit-Comment-API/

│

├── app/

│   ├── \_\_init\_\_.py

│   ├── main.py

│   ├── routes.py

│   ├── schemas.py

│   ├── prompts.py

│   ├── llm.py

│   ├── models.py

│   └── database.py

│

├── .env

├── requirements.txt

├── README.md

└── .venv/

File Responsibilities

main.py



Initializes the FastAPI application and registers the API routes.



routes.py



Contains the API endpoints.



schemas.py



Defines request and response data structures using Pydantic.



prompts.py



Contains the prompt engineering logic used to instruct the Gemini model.



llm.py



Handles communication with the Gemini API.



models.py



Defines the database models.



database.py



Configures the SQLite database and SQLAlchemy session.



7\. API Endpoints

POST /generate-comment



Generates a new AI comment.



Request

{

&#x20; "platform": "reddit",

&#x20; "post\_title": "How to prepare for UPSC?",

&#x20; "post\_content": "What is the best strategy for starting UPSC preparation?",

&#x20; "community": "UPSC"

}

Response

{

&#x20; "platform": "reddit",

&#x20; "comment": "Honestly, the best way to start is by thoroughly reading the syllabus and analyzing the last few years of PYQs. It gives you a clear idea of what UPSC actually asks..."

}

GET /comments



Returns previously generated comments stored in the database.



Example response

\[

&#x20; {

&#x20;   "id": 1,

&#x20;   "platform": "reddit",

&#x20;   "community": "UPSC",

&#x20;   "post\_title": "UPSC preparation tips",

&#x20;   "post\_content": "What is the best way to prepare for UPSC?",

&#x20;   "generated\_comment": "Honestly, start with the syllabus and PYQs...",

&#x20;   "created\_at": "2026-08-13T07:06:28"

&#x20; }

]

GET /comments/{comment\_id}



Returns a specific generated comment using its ID.



Example

GET /comments/2



If the comment exists, the API returns its stored details.



If it does not exist:



{

&#x20; "detail": "Comment not found"

}

DELETE /comments/{comment\_id}



Deletes a stored comment using its ID.



Example

DELETE /comments/2



If the comment does not exist:



{

&#x20; "detail": "Comment not found"

}

8\. API Documentation



FastAPI automatically provides interactive Swagger documentation.



After starting the server, open:



http://127.0.0.1:8000/docs



The OpenAPI specification is available at:



http://127.0.0.1:8000/openapi.json



Swagger can be used to test all API endpoints without requiring a separate frontend.



9\. How to Run the Project

Step 1: Clone the project

git clone <your-github-repository-url>

Step 2: Open the project

cd Reddit-Comment-API

Step 3: Create a virtual environment

python -m venv .venv

Step 4: Activate the virtual environment



Windows:



.venv\\Scripts\\activate

Step 5: Install dependencies

pip install -r requirements.txt

Step 6: Configure the Gemini API key



Create a .env file:



GEMINI\_API\_KEY=your\_api\_key\_here



Do not commit the .env file to GitHub.



Step 7: Start the server

python -m uvicorn app.main:app --reload



The API will run at:



http://127.0.0.1:8000



Swagger documentation:



http://127.0.0.1:8000/docs

10\. Example Workflow



A user finds a post on Reddit:



Title:

How to stay consistent with UPSC preparation?



Content:

I keep losing motivation while preparing. What should I do?



Community:

UPSC



The application sends this information to:



POST /generate-comment



The API creates a structured prompt.



The prompt is sent to Gemini.



Gemini generates a natural response.



The generated response is returned to the user.



The generated comment is also stored in SQLite.



The user can then copy the comment and use it on the social media platform.



11\. Prompt Engineering



The application uses a structured prompt instead of sending the post directly to the AI model.



The prompt contains:



Platform

Community

Post title

Post content



The AI is also given rules such as:



Write one natural comment.

Do not sound like an advertisement.

Do not mention that the response was generated by AI.

Keep the comment concise.

Match the platform's tone.

Return only the comment.



This helps produce comments that are more relevant to the original conversation.



12\. Database



The project uses SQLite for storing generated comments.



Each stored comment contains information such as:



ID

Platform

Community

Post title

Post content

Generated comment

Created time



Example:



{

&#x20; "id": 3,

&#x20; "platform": "linkedin",

&#x20; "community": "careers",

&#x20; "post\_title": "Importance of consistency in career growth",

&#x20; "post\_content": "How can someone consistently improve their professional skills?",

&#x20; "generated\_comment": "For me, the key is shifting from massive sessions to daily micro-habits...",

&#x20; "created\_at": "2026-08-13T07:13:05"

}

13\. Validation Testing



The API was tested with incomplete requests.



For example, when post\_content is missing:



{

&#x20; "platform": "reddit",

&#x20; "post\_title": "UPSC preparation",

&#x20; "community": "UPSC"

}



FastAPI correctly returns:



422 Unprocessable Content



This confirms that required request fields are being validated.



14\. Error Handling Testing



The API was also tested with non-existing comment IDs.



Example:



GET /comments/9999



Response:



{

&#x20; "detail": "Comment not found"

}



Similarly:



DELETE /comments/9999



returns:



{

&#x20; "detail": "Comment not found"

}



This confirms that invalid database IDs are handled correctly.



15\. Platform Testing



The API has been tested with different platforms.



Reddit



Example context:



Community: UPSC



The generated comment follows a conversational Reddit-style response.



LinkedIn



Example context:



Community: careers



The generated comment is more professional and career-oriented.



This demonstrates that the platform information can influence the generated response.



16\. Current Project Status



The following major components have been implemented:



&#x20;Python project setup

&#x20;Virtual environment

&#x20;FastAPI

&#x20;Gemini integration

&#x20;Prompt engineering

&#x20;Comment generation

&#x20;SQLite database

&#x20;SQLAlchemy

&#x20;Save generated comments

&#x20;Get all comments

&#x20;Get individual comment

&#x20;Delete comment

&#x20;Request validation

&#x20;Error handling

&#x20;Reddit testing

&#x20;LinkedIn testing

&#x20;Multiple input testing

&#x20;Swagger API documentation

&#x20;Comprehensive API testing

17\. Future Improvements



Possible future improvements include:



Frontend



Create a simple web interface where users can paste a social media post and click:



Generate Comment

More Platforms



Support additional platforms such as:



X

LinkedIn

Reddit

Other social platforms

Multiple Comment Suggestions



Instead of generating one comment, the system could generate several options:



1\. Professional

2\. Casual

3\. Short

4\. Detailed

Authentication



Add user authentication so each user can maintain their own comment history.



Deployment



Deploy the API to a cloud platform so it can be accessed remotely.



Social Media Integration



In a future version, the application could integrate with official social media APIs where permitted.



18\. Conclusion



The AI Comment Generation API demonstrates how Generative AI can be integrated with a REST API to automate social media comment drafting.



The system accepts contextual information about a social media post, generates a relevant comment using Gemini, returns the result through FastAPI, and stores the generated comment in a SQLite database.



The project combines:



REST API

\+

Generative AI

\+

Prompt Engineering

\+

Database

\+

Validation

\+

API Testing



to create a functional AI-powered comment generation system.





\### After pasting



Save it with:



\*\*Ctrl + S\*\*



Then close Notepad.



From your project folder, run:



```cmd

dir



You should now see:



README.md

requirements.txt

app

.venv

