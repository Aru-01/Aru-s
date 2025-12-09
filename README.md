# 🌟 Aru's - E-Commerce API

A modern, **feature-rich e-commerce backend** built with Django and Django REST Framework.  
Designed to handle users, products, reviews, carts, and orders efficiently with **JWT authentication, nested endpoints, and Swagger API documentation**. Perfect for learning, testing, or building scalable e-commerce applications.

---

## 🚀 Features

- **User Management & Authentication**

  - JWT-based authentication using Djoser.
  - Custom registration for extended user profiles.
  - Role-based access control for admin and regular users.

- **Products & Categories**

  - CRUD operations for products and categories.
  - Product images with size validation (max 10MB).
  - Advanced search, filter, and ordering capabilities.
  - Nested product review system.

- **Cart & Cart Items**

  - UUID-based carts for each user.
  - Nested endpoints to manage cart items.
  - Automatic total price calculation.
  - Restricted access for security.

- **Orders**

  - Convert cart to order with validation and cleanup.
  - Transaction-safe operations for reliability.
  - Status management and role-based permissions.
  - Full order lifecycle support.

- **Product Reviews**

  - Nested under products.
  - Author-only edit/delete permissions.
  - Secure and enhanced serializer logic.

- **API Documentation**
  - Integrated Swagger UI for easy exploration.
  - Custom descriptions and endpoint summaries.

---

## 💻 Technology Used

- **Django 4.3** (Backend framework)
- **Django REST Framework** (API development)
- **Djoser** (Authentication)
- **drf-yasg** (Swagger API Documentation)
- **PostgreSQL / SQLite** (Database)
- **JWT Tokens** for secure authentication

---

## ⚡ Installation Process

```bash
# Clone the repository
git clone <your-repo-url>
cd <your-project-dir>

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## API Documentation

Swagger documentation is available at:

```
http://127.0.0.1:8000/swagger/
```

ReDoc documentation is available at:

```
http://127.0.0.1:8000/redoc/
```

## Environment Variables

Create a `.env` file in the root directory and add the following:

```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
ALLOWED_HOSTS=*
EMIL_HOST=your_email_host
```

## License

This project is licensed under the MIT License.

---

### Author

[MD. ARIFUL ISLAM](https://github.com/Aru-01)
