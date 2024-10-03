# LMS Project

A Learning Management System (LMS) built using Django, Docker, and PostgreSQL.

## Current Status

**Day 1 Completed:**
- Initialized Django project.
- Set up PostgreSQL as the database.
- Configured Docker to run the application in containers.
- Basic project structure established.

## Project Setup Instructions

### Prerequisites

Ensure you have the following installed on your machine:
- **Docker**: To run the project in containers.
- **Git**: For version control.
- **Python 3.9+**: (Optional, if running outside Docker).

### Cloning the Repository

To get started, clone the repository:

```bash
git clone https://github.com/HubertFijolek1/lms_project.git
cd lms_project
```

### setting up the project

the project is containerized using docker. follow these steps to get everything running:

1. **install docker** (if not installed):  
   [install docker](https://www.docker.com/get-started)

2. **build and run the containers**:

```bash
docker-compose up --build
```

3. **apply Django Migrations: Once the containers are running, apply the initial Django migrations to set up the database schema:

```bash
docker-compose exec web python manage.py migrate
```

4. **Access the Development Server: The application will be available at http://localhost:8000.

### project structure

after day 1, the project structure looks like this:

```arduino
lms_project/
├── docker/
│   ├── docker-compose.yml
│   ├── dockerfile
│   ├── requirements.txt
├── lms_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── db.sqlite3  (if using sqlite for dev)
└── .gitignore
```

### technologies used

- **django 4.2.16**: python web framework.
- **postgresql 13**: database system.
- **docker**: containerization tool for consistent development environments.

### next steps

- implement user authentication.
- set up role-based access control (rbac) for different types of users (student, teacher, admin).

### troubleshooting

if you encounter any issues, ensure docker is running and the `docker-compose.yml` file is correctly set up. you can also check the container logs:

```bash
docker-compose logs
```

You can stop the containers using:

```bash
docker-compose down
If you need to rebuild the containers after changes, use:
```

```bash
docker-compose up --build
```

For further debugging, it's helpful to check the individual service logs (e.g., web or database):

```bash
docker-compose logs <service-name>
Replace <service-name> with the appropriate container name, such as web or db.
```

### Common Issues

1. **Database connection errors**:
   - Ensure PostgreSQL is running inside the container.
   - Verify the database connection details in the `settings.py` file, particularly the `DATABASES` section.
   
2. **Docker permission issues**:
   - On Linux, you may need to run Docker commands with `sudo` if your user isn’t in the Docker group.

3. **Static files not loading**:
   - Make sure the `STATIC_URL` and `STATICFILES_DIRS` are correctly configured in `settings.py`.
   - Run the following command to collect static files:

   ```bash
   docker-compose exec web python manage.py collectstatic
   ```

### additional resources

- [django documentation](https://docs.djangoproject.com/)
- [docker documentation](https://docs.docker.com/)
- [postgresql documentation](https://www.postgresql.org/docs/)

for further assistance, you can also check community forums or raise issues on the project repository.

happy coding!
