# 02 - Authentication & User Management

## 🔐 1. Authentication Overview
The application uses a stateless **JWT (JSON Web Token)** authentication system to secure endpoints and manage user sessions.

## 🚶 2. User Flows

### A. Signup Flow
1.  User provides `username`, `email`, and `password`.
2.  Backend hashes the password (using `passlib` with `bcrypt`).
3.  User details are saved to the database (SQLAlchemy/PostgreSQL or SQLite for simplicity).
4.  Redirect to Login page.

### B. Login Flow
1.  User provides credentials.
2.  Backend validates credentials against the hashed password.
3.  On success, backend generates a JWT token containing the `user_id`.
4.  Token is returned to the frontend.

## 🛠️ 3. Implementation Details

### JWT Configuration
*   **Secret Key**: Loaded from `.env`.
*   **Algorithm**: `HS256`.
*   **Expiration**: 60 minutes (extendable).

### Backend Security
*   Use `FastAPI` dependency injection for protecting routes.
*   Example:
    ```python
    @app.get("/api/query")
    async def run_query(current_user: User = Depends(get_current_user)):
        # Only accessible if a valid JWT is provided in the header
        ...
    ```

### Frontend Token Management
*   Store JWT in `localStorage` or `sessionStorage`.
*   Include the token in the `Authorization` header for every request:
    `Authorization: Bearer <token>`

## 🛡️ 4. Security Requirements
*   **Password Hashing**: Use `bcrypt`.
*   **Input Validation**: Use Pydantic models to validate all incoming auth data.
*   **Error Messages**: Avoid specific error messages (e.g., "User not found") to prevent account enumeration. Use generic "Invalid credentials".

---
> [!WARNING]
> Never store the JWT Secret Key in the code. Ensure it is only available via environment variables.
