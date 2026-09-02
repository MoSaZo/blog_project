# Blog Project

A simple blog application built with Django.

## Features

- Create blog posts
- Publish and draft posts
- News management
- Comment system
- Jalali Date support
- Django Admin Panel

## Tech Stack

- Python 3.x
- Django 6
- SQLite
- django-jalali

## Project Structure

```
blog_project/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
├── manage.py
└── db.sqlite3
```

## Installation

Clone the repository

```bash
git clone https://github.com/MoSaZo/blog_project.git
```

Install dependencies

```bash
pip install django django-jalali
```

Run migrations

```bash
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

## Models

### Post

- Title
- Content
- Author
- Slug
- Status
- Created Date
- Updated Date

### News

- Title
- Content
- Active Status

### Comment

- Related Post
- Author
- Status

## Future Improvements

- REST API
- Authentication
- Search
- Categories
- Tags
- Pagination
- Docker
- Unit Tests
- GitHub Actions
- Swagger

## License

MIT

## Author

MoSaZo
