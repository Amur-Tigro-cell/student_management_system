```markdown
# Student Management System

A simple Django-based web application for managing student records. Users can add, view, edit, and delete student information through a clean web interface.

## Features

- Add new student records
- View all students
- View individual student details
- Edit student information
- Delete student records
- Django SQLite database
- Static CSS styling
- Admin panel support

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```text
student_management_system/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── sms_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── student_management/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## Prerequisites

Make sure Python 3.10 or newer is installed.

Check Python:

```bash
python --version
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Amur-Tigro-cell/student_management_system.git
cd student_management_system
```

### 2. Create and activate a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Django Admin

Create an administrator account:

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

## Student Information

The project includes a `Student` model that supports storing student information such as:

- Name
- Age
- Department
- Personal information

The exact fields can be customized in:

```text
sms_app/models.py
```

## Running Tests

```bash
python manage.py test
```

## Author

Amur-Tigro-cell

## License

This project is available for educational and personal use.
```
