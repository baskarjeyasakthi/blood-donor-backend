# 🩸 Blood Donor Management System - Backend

A RESTful backend application for the Blood Donor Management System built using **Django**, **Django REST Framework**, and **PostgreSQL**.

The backend provides APIs for donor registration, donor management, and admin operations.

## 🚀 Features

- Donor Registration API
- View Donor Details
- Update Donor Information
- Delete Donor Information
- Admin Login API
- PostgreSQL Database
- RESTful API Architecture

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- Django ORM

## 📂 Project Structure

```
myproject/
│
├── donorapp/
├── myproject/
├── manage.py
├── requirements.txt
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/baskarjeyasakthi/blood-donor-backend.git
```

Go to the project folder:

```bash
cd blood-donor-backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

The backend server will run at:

```
http://127.0.0.1:8000/
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/donor/` | Get all donors |
| POST | `/api/donor/` | Add a donor |
| PUT | `/api/donor/<id>/` | Update donor |
| DELETE | `/api/donor/delete/<id>/` | Delete donor |
| POST | `/api/admin-login/` | Admin login |

## 👨‍💻 Author

**Jeyasakthi Baskar**

GitHub: https://github.com/baskarjeyasakthi
