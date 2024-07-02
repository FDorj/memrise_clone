# Memrise Clone Project

This project is a simplified version of a learning platform similar to Memrise. It allows users to select topics, view lessons, complete exercises, and track their progress.

## Features

1. **Learning Module:**
   - Users can select a topic from a list of available topics.
   - View detailed lessons for each topic.
   - Complete exercises related to the lessons.

2. **Progress Tracking:**
   - Users can track their progress for each lesson.
   - View detailed statistics and receive recommendations based on performance.

## Requirements

- Python 3.10
- Django 5.0.6
- MySQL

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/FDorj/memrise_clone.git
cd memrise_clone
```

### 2. Create a Virtual Environment and Activate It

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database

- Install MySQL and set up a new database.
- Update the `DATABASES` setting in `memrise_clone/settings.py` with your MySQL credentials.

### 5. Apply Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python3 manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python3 manage.py runserver
```

Open your web browser and go to `http://127.0.0.1:8000/group2/select-topic/` to start using the platform.

## Directory Structure

```
memrise_clone/
├── group2/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── group2/
│   │       ├── get_username.html
│   │       ├── select_topic.html
│   │       ├── view_lesson.html
│   │       ├── complete_exercise.html
│   │       ├── search.html
│   │       ├── search_results.html
│   │       └── review_progress.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── memrise_clone/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Models

### User

Represents a user in the system.

### Lesson

Represents a lesson within a topic.

### Exercise

Represents an exercise related to a lesson.

### Progress

Tracks the user's progress through lessons and exercises.

### LessonCompletion

Tracks the completion of lessons by users.

### Search

Handles searching for lessons based on keywords.

## Views

### get_username

Handles user login based on the username.

### select_topic

Displays a list of available topics.

### view_lesson

Displays the details of a lesson and its related exercises.

### search_lesson

Allows users to search for lessons using keywords.

### review_progress

Displays the user's progress, detailed statistics, and recommendations.

### complete_exercise

Handles the completion of exercises and updates the user's progress.

## URLs

- `/group2/get-username/`: Enter username to start.
- `/group2/select-topic/`: Select a topic.
- `/group2/view-lesson/<int:lesson_id>/`: View lesson details and exercises.
- `/group2/complete-exercise/<int:exercise_id>/`: Complete an exercise.
- `/group2/search-lesson/`: Search for lessons.
- `/group2/review-progress/<int:user_id>/`: Review progress.

## Templates

- `get_username.html`: Form to enter the username.
- `select_topic.html`: Displays available topics.
- `view_lesson.html`: Displays lesson details and exercises.
- `complete_exercise.html`: Form to complete an exercise.
- `search.html`: Form to search for lessons.
- `search_results.html`: Displays search results.
- `review_progress.html`: Displays progress, detailed statistics, and recommendations.

## Running Tests

To run the tests, execute:

```bash
python3 manage.py test
```

This will run all the tests defined in `group2/tests.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.