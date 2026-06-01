
# 🎮 GamerHUB API

A backend REST API for gamers built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

GamerHUB allows users to discover games, write reviews, like reviews, add favorites, and manage accounts with secure JWT authentication.

---

## 🚀 Features

### 👤 User Management
- User Registration
- User Login
- Password Hashing
- JWT Authentication
- Protected Routes

### 🎮 Games
- Add Games
- Get All Games
- Get Single Game
- Update Game Details
- Delete Game

### 📝 Reviews
- Add Reviews
- View Reviews
- Update Reviews
- Delete Reviews

### ❤️ Likes
- Like Reviews
- Remove Likes

### ⭐ Favorites
- Add Games to Favorites
- Remove Favorites
- View Favorite Games

### 🔒 Security
- OAuth2 Authentication
- JWT Tokens
- Password Hashing using Passlib
- Dependency Injection for Protected Routes

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python

### Database
- PostgreSQL
- SQLAlchemy ORM

### Authentication
- JWT
- OAuth2PasswordBearer
- Passlib

### API Documentation
- Swagger UI
- ReDoc

---

## 📂 Project Structure

```bash
GamersHUB/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── oauth2.py
├── jwttoken.py
├── requirement.txt
│
└── routers/
    ├── users.py
    ├── login.py
    ├── games.py
    ├── reviews.py
    ├── favorite.py
    ├── like.py
    ├── comment.py
    ├── hasshing.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/GamerHUB.git
cd GamerHUB
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirement.txt
```

---

## 🗄️ Database Setup

Create PostgreSQL Database:

```sql
CREATE DATABASE gamerhub;
```

Update your database URL in:

```python
database.py
```

Example:

```python
DATABASE_URL = "postgresql://username:password@localhost/gamerhub"
```

---

## ▶️ Run Project

```bash
uvicorn main:app --reload
```

API will run at:

```bash
http://127.0.0.1:8000
```

Swagger Documentation:

```bash
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```bash
http://127.0.0.1:8000/redoc
```

---

## 🔑 Authentication Flow

1. Register User
2. Login User
3. Receive JWT Token
4. Authorize in Swagger
5. Access Protected Routes

---

## 📌 Future Improvements

- Admin Panel
- Game Categories
- Search & Filtering
- Pagination
- Profile Pictures
- Recommendation System
- Game Rating System
- Redis Caching
- Docker Support
- CI/CD Pipeline

---

## 👨‍💻 Author

**Pranav Chaudhari**

B.Tech CSE (AI & ML)

FastAPI | PostgreSQL | Machine Learning | AI Engineering

GitHub: https://github.com/PranavChaudhari009
