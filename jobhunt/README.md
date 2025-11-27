# Job Hunt Web App

A Django-based web application to help users track their job hunting activities, including jobs, applications, interviews, and statistics.

## Features

- **Dashboard**: Overview of total jobs, applications, and upcoming interviews with summary tables.
- **Job Management**: Add, view, and manage job listings.
- **Application Tracking**: Track job applications with status, type, platform, and response updates.
- **Interview Logging**: Record and view interview details.
- **Statistics**: Analyze application success rates by type and platform.
- **Admin Interface**: Full Django admin for data management.
- **Responsive Design**: Clean, green-themed UI with light grey accents.

## Models

- **City**: Locations for companies.
- **Company**: Organizations posting jobs.
- **Job**: Job listings with title, company, link, and summary.
- **Application**: Job applications with date, type, status, platform, and response tracking.
- **Interview**: Interview records linked to applications.
- **Type**: Application types (e.g., mail pitch, spontaneous, offer).
- **Platform**: Job posting platforms.
- **Status**: Application statuses.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd jobhunt
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv jobhunt-env
   source jobhunt-env/bin/activate  # On Windows: jobhunt-env\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install django
   ```

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the app at `http://127.0.0.1:8000/`

## Usage

- **Dashboard**: Main overview page.
- **Add Forms**: Use navigation links to add companies, jobs, applications, and interviews.
- **View Lists**: Access lists for jobs, applications, and interviews.
- **Details**: Click detail links to view individual records and update application status.
- **Stats**: Analyze application success rates.
- **Admin**: Manage data via `/admin/` with superuser credentials.

## Key Features

- **Prefilled Forms**: Adding a job redirects to add application with the job pre-selected.
- **Status Updates**: Update application status and response directly from detail pages.
- **Upcoming Interviews**: Dashboard shows only future interviews.
- **Empty States**: Friendly messages when lists are empty.
- **Navigation**: Consistent navbar across all pages.

## Technologies

- Django 5.2
- SQLite (default database)
- HTML/CSS for frontend
- Bootstrap-inspired styling

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes and test.
4. Submit a pull request.

## License

This project is open-source. Use at your own risk.
