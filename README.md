# 🚀 FastAPI Practice: Social Media API

This repository is dedicated to my practice and progress through the **FastAPI Python API Development** course. I am building a full-featured social media backend from scratch.

## 📌 Project Features
The application is a social media platform API where users can:
* **User Management:** Register and login with secure hashed passwords.
* **Authentication:** JWT (JSON Web Token) based login and protected routes.
* **Post Management:** Create, read, update, and delete (CRUD) their own posts.
* **Voting System:** Like/Vote on other users' posts.
* **Database Integration:** Persistent storage using PostgreSQL.

## 🛠️ Tech Stack
* **Framework:** FastAPI
* **Validation:** Pydantic
* **ORM:** SQLAlchemy
* **Database:** PostgreSQL
* **Migrations:** Alembic
* **Testing:** Pytest
* **Deployment:** Docker & GitHub Actions

## 🏗️ Folder Structure
```text
.
├── app/
│   ├── routers/       # Modular route handlers (posts, users, auth, votes)
│   ├── main.py        # Entry point of the API
│   ├── models.py      # SQLAlchemy database models
│   ├── schemas.py     # Pydantic data validation models
│   ├── database.py    # Database connection setup
│   ├── oauth2.py      # JWT authentication logic
│   └── utils.py       # Password hashing and helper functions
├── tests/             # Automated test cases
├── alembic/           # Database migration files
├── .env               # Environment variables (Secrets)
└── requirements.txt   # Project dependencies
