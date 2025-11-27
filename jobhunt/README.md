# Job Hunt Web App

A Django-based web application to help users track their job hunting activities, including jobs, applications, interviews, and statistics.

## Features

- **Dashboard**: Overview of total jobs, applications, and upcoming interviews with summary tables.
- **Job Management**: Add, view, and manage job listings.
- **Application Tracking**: Track job applications with status, type, platform, and response updates.
- **Interview Logging**: Record and view interview details.
- **Statistics**: Analyze application success rates by type and platform.
- **Admin Interface**: Full Django admin for data management.

## Models

- **City**: Locations for companies.
- **Company**: Organizations posting jobs.
- **Job**: Job listings with title, company, link, and summary.
- **Application**: Job applications with date, type, status, platform, and response tracking.
- **Interview**: Interview records linked to applications.
- **Type**: Application types (e.g., mail pitch, spontaneous, offer).
- **Platform**: Job posting platforms.
- **Status**: Application statuses.

## Usage

- **Dashboard**: Main overview page.
- **Add Forms**: Use navigation links to add companies, jobs, applications, and interviews.
- **View Lists**: Access lists for jobs, applications, and interviews.
- **Details**: Click detail links to view individual records and update application status.
- **Stats**: Analyze application success rates.
- **Admin**: Manage data via `/admin/` with superuser credentials.

## Technologies

- Django 5.2
- SQLite (default database)
- HTML/CSS for frontend
- Bootstrap-inspired styling
