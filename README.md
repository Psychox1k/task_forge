# Task Forge
Task Forge is a Django application for project and task management in IT teams.

## Features
- Manage users (Workers with Positions)
- Create and manage projects
- Teams with members and leaders
- Tasks with priorities, types, and tags
- Admin panel management
- Unit tests (admin, forms, models, views)

## Tech Stack
- Python 3.12
- Django 5.2
- crispy-forms + bootstrap5
- django-select2
- pytest/unittest

## Design
- Soft UI Desgin System


## Installation
```bash
git clone https://github.com/Psychox1k/task_forge.git
cd task_forge
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## Running tests
```bash
python manage.py test
```

## Authors
- [Psychox1k](https://github.com/Psychox1k)(Kyrylo Zhyhariev)