# Phase 2: Authentication & User Management

## 🎯 Goal
Implement secure user signup, login, and JWT-based session management.

## 🛠️ Tasks

### 1. Database Setup
- Set up a simple database (SQLite for development, PostgreSQL for production).
- Create `User` model with fields: `id`, `username`, `email`, `hashed_password`.

### 2. Password Security
- Implement password hashing using `passlib` with `bcrypt`.
- Create utility functions: `hash_password(password)` and `verify_password(plain, hashed)`.

### 3. JWT Logic
- Implement `create_access_token(data)` using `python-jose`.
- Configure `SECRET_KEY` and `ALGORITHM` in `.env`.

### 4. API Endpoints
- **POST `/api/auth/signup`**: Validate user data, hash password, and save to DB.
- **POST `/api/auth/login`**: Verify credentials and return a Bearer JWT.
- **GET `/api/auth/me`**: A protected route that returns the current user profile.

### 5. Middleware / Dependencies
- Create a `get_current_user` dependency in FastAPI to secure future routes (like `/api/query`).

## ✅ Success Criteria
- [ ] Users can register with valid email/password.
- [ ] Login returns a valid JWT token.
- [ ] Accessing `/api/auth/me` without a token results in a `401 Unauthorized` error.
