# 🚀 FastAPI Social Media API

A production-oriented social media backend built using **FastAPI**.  
This project is being developed to implement secure authentication, relational database modeling, and scalable REST API architecture.

> Status: 🚧 Active Development

---

## 📌 Project Vision

This backend system is designed to support:

- User registration with secure password hashing
- JWT-based authentication & protected routes
- CRUD operations for posts
- Voting/like system (many-to-many relationships)
- PostgreSQL persistent storage
- Database migrations using Alembic
- Docker-based deployment
- Automated testing with Pytest

The objective is to follow production-style architecture and clean backend design principles.

---

## 🛠 Technology Stack

| Layer | Technology |
|-------|------------|
| API Framework | FastAPI |
| Validation | Pydantic |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Migrations | Alembic |
| Testing | Pytest |
| Containerization | Docker |
| CI/CD | GitHub Actions |

---

## 📂 Current Repository Structure

```text
.
├── venv/                 # Local Python virtual environment (not for production)
├── .gitignore            # Git exclusion rules
├── README.md             # Project documentation
└── SECURITY.md           # Security policy
```

> ⚠️ Note: The `venv/` directory should not be committed in production repositories. It is environment-specific and must be included in `.gitignore`.

---

## 🐍 Local Development Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vaibhav-S-Gowda/fastapi-playground.git
cd fastapi-playground
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Linux / macOS**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

*(requirements.txt will be introduced in the next development phase.)*

---

## 🔐 Security

Security policies and vulnerability reporting guidelines are defined in:

```
SECURITY.md
```

---

## 📈 Development Roadmap

Upcoming milestones:

- Introduce structured `app/` directory
- Implement database configuration
- Add authentication system
- Create modular routers
- Integrate Alembic migrations
- Add test suite
- Dockerize the application
- Configure CI pipeline

---

## 🎯 Purpose

This repository serves as:

- A backend architecture learning project
- A portfolio-ready FastAPI implementation
- A demonstration of secure API development practices
- A foundation for production-grade backend systems

---

## 📄 License

This project is intended for educational and development purposes.
