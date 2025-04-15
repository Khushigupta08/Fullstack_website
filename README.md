# Fullstack_website
# AI Website Builder
This project is an AI-powered website builder built with Django and Django REST Framework. It allows users to sign up/login using JWT-based authentication and generate website layouts/content using DeepAI and Cohere APIs. The project has two main Django apps:

- `users` – Handles user registration and JWT authentication.
- `websites` – Handles AI-driven website generation, layout saving, and content generation using external APIs.

---

##  Features

- JWT Authentication using Django REST Framework Simple JWT
- Website layout and content generation via AI APIs (DeepAI, Cohere)
- Modular app structure
- RESTful API endpoints

---

## Tech Stack

- Backend: Django, Django REST Framework
- Authentication: JWT (Simple JWT)
- External APIs: DeepAI, Cohere
- Language: Python

---

## 🛠️ Setup Instructions

Follow the steps below to clone and run this project on your local system:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai_website_builder.git
cd ai_website_builder
### 2. Create Virtual Environment and Activate
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
### 3   Install Dependencies
pip install -r requirements.txt
### 4 Set Up Environment Variables
COHERE_API_KEY=your_cohere_api_key

### 5 Run Migrations
python manage.py makemigrations
python manage.py migrate
### 6 Run the Server
python manage.py runserver
