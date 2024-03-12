# tic-tac-toe-django
Simple tic tac toe game using Django with Docker Compose for easy development and deployment.

## Prerequisites

- Docker: [Installation instructions](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation instructions](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/shivamx512/tic-tac-toe-django
    ```

2. Navigate to the project directory:

    ```bash
    cd tic_tac_toe
    ```

3. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

4. Access the Django application:

    Open your web browser and go to http://0.0.0.0:8000/

5. To stop the containers, press `Ctrl + C` in the terminal where `docker-compose` is running.

## Project Structure

- `docker-compose.yml`: Configuration file for Docker Compose.
- `Dockerfile`: Dockerfile for the Django application.
- `requirements.txt`: Python dependencies for the Django application.
- `tic_tac_toe/`: Django project directory.
    - `settings.py`: Django settings file.
    - `urls.py`: Django URL configuration file.
    - `views.py`, `models.py`, `forms.py`, etc.: Django application files.
- `manage.py`: Django management script.
- `README.md`: Project documentation (you're reading it right now).
- `.gitignore`: Git ignore file.

## Docker Compose Commands

- `docker-compose up --build`: Build and start the Docker containers.
- `docker-compose down`: Stop and remove the Docker containers.
- `docker-compose exec web python manage.py migrate`: Run Django database migrations.
- `docker-compose exec web python manage.py createsuperuser`: Create a Django superuser.
