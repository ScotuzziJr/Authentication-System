# Django and React Authentication System

This project implements a secure authentication system using Django as the backend and React as the frontend. The backend utilizes Django REST Framework (DRF) and SimpleJWT for token-based authentication, with JWT tokens stored in HTTP-only cookies for enhanced security.

## Features

- **User Registration**: Users can register with a username, email, and password.
- **Login**: Secure login with JWT access and refresh tokens.
- **Logout**: Tokens are invalidated by clearing cookies.
- **Token Refresh**: Access tokens can be refreshed using the refresh token stored in cookies.
- **Authenticated Endpoints**: Users can fetch their private data (e.g., notes) after logging in.
- **Custom Authentication**: Uses cookies to store and validate JWT tokens.

## API Endpoints

### Base URLs
- **Admin Panel**: `/admin/`
- **API Base**: `/api/`

### Authentication Endpoints
- **Login**: `POST /api/token/`  
  Obtain access and refresh tokens.
- **Refresh Token**: `POST /api/token/refresh/`  
  Refresh access tokens using the refresh token.
- **Logout**: `POST /api/logout/`  
  Log out by clearing cookies.
- **Register**: `POST /api/register/`  
  Create a new user account.
- **Check Authentication**: `POST /api/authenticated/`  
  Verify if the user is authenticated.

### Notes Endpoints
- **Fetch Notes**: `GET /api/notes/`  
  Retrieve all notes for the logged-in user.

## Project Structure

- **Models**: Defines `Note` model with a foreign key relationship to the `User`.
- **Serializers**: Includes serializers for user registration, notes, and authentication.
- **Views**: Implements views for handling authentication, registration, and fetching user-specific data.
- **URLs**: Organizes routes for the API and application.

## Authentication Flow

1. **Login**:
   - Users log in using their username and password.
   - Access and refresh tokens are returned in HTTP-only cookies.

2. **Token Validation**:
   - Securely validate tokens from cookies using custom authentication.

3. **Token Refresh**:
   - Renew access tokens via the refresh token stored in cookies.

4. **Logout**:
   - Clear cookies to log out the user.

## Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework
- Django REST Framework SimpleJWT

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ScotuzziJr/Authentication-System
   cd Authentication-System
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Admin Panel**:
   - Create a superuser:
     ```bash
     python manage.py createsuperuser
     ```
   - Visit `/admin/` to log in with the superuser credentials.

## Security Considerations

- Tokens are stored in HTTP-only cookies to prevent access via JavaScript.
- Cookies are marked `Secure` and `SameSite=None` to allow cross-site requests over HTTPS.

## License

This project is licensed under the MIT License.
