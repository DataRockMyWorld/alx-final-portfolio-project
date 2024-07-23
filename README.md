# WorkSafe Application - README.md

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [User Roles and Permissions](#user-roles-and-permissions)
- [Models and Database Schema](#models-and-database-schema)
- [Forms and Validations](#forms-and-validations)
- [API Integration](#api-integration)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
WorkSafe is a comprehensive Health, Safety, Security, and Environment (HSSE) management application designed to help organizations manage their safety protocols efficiently. It provides functionalities for employees to fill out various HSSE forms, track performance metrics, and allows HSSE Managers to oversee and approve documents and submissions.

## Features
- User authentication and authorization
- Dashboard with performance metrics
- Form submissions for various HSSE-related activities
- Document management system with upload and download functionalities
- KPI tracking and dashboard
- Real-time notifications for approvals
- Responsive UI/UX using Bootstrap

## Technologies Used
- **Backend:** Django 4.2, Python 3.8
- **Frontend:** Bootstrap, HTML, CSS, JavaScript
- **Database:** SQLite (for development), PostgreSQL (for production)
- **APIs:** Google Maps API for location data
- **Others:** Django REST Framework, WeasyPrint (for PDF export), Chart.js (for data visualization)

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.2
- Git
- Virtualenv


### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/WorkSafe.git
   cd WorkSafe
   ```

2. **Create virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\\Scripts\\activate`
    ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the server**
   ```bash
   python manage.py runserver
   ```

## Usage

### User Registration and Login

* Users can register and login via the /register/ and /login/ URLs.
* HSSE Managers can approve new user registrations.

### Dashboard

* Users have access to a personal dashboard that displays their performance metrics and form submissions.
* HSSE Managers have an admin dashboard to oversee all activities.

### Form Submissions

* Users can fill out the form and submit it to the database.
* Forms include Work Completion Form, Toolbox form

### Document Management

* HSSE Manager can upload and download documents.
* All users can view and download documents

### KPI Tracking and Dashboard

* Users can track their KPIs and view their performance metrics.
* HSSE Manager can view all KPIs and their performance metrics
* HSSE Manager can set target KPIs in the admin dashboard

### User Roles and Permissions

* Users can access the dashboard, form submissions, and document management.
* HSSE Managers can view and approve form submissions, manage documents, and set KPIs.

## Models and Database Schema

### User Model
*   `username`
*   `email`
*   `password`
*   `first_name`
*   `last_name`
*   `department`
*   `profile_image`
*   `is_hsse_manager`

#### Form Model
*   `omc`
*   `time_commenced`
*   `time_completed`
*   `duration`
*   `material_used`
*   `quantity`
*   `number_of_workmen`
*   `hours_worked`
*   `kilometers_traveled`
*   `lost_time_incidents`
*   `medical_treatment_cases`
*   `first_aid_cases`
*   `oil_spilled`
*   `site_comment`
*   `google_address`

### IncidentReport

* `site`
* `date`
* `time`
* `incident_type`
* `impact_type`
* `details`
* `location`
* `immediate_action`
* `status`
* `incident_number`
* `latitude`
* `longitude`

### KPI Model

* `date`
* `objective`
* `kpi_name`
* `category`
* `target_value`

### Forms and Validations

*   WorkCompletionFormForm
*   ToolboxTalkFormForm
*   IncidentReportForm
*   Each form has client-side and server-side validation for required fields and data types.


### API Integration

*   Google Maps API: Used to auto-complete and validate addresses in form submissions.


### Testing

*   Unit Tests: Implemented using Django's built-in testing framework.
*   Test Coverage: Ensure high test coverage for views, models, and forms.

```bash
python manage.py test
```

### Contributing

We welcome contributions to the WorkSafe project. Please fork the repository and create a pull request with your changes. 
Ensure that your code adheres to the project's coding standards and includes appropriate tests.

### License

WorkSafe is licensed under the MIT License. See the LICENSE file for more information.

### Acknowledgements

We would like to thank all contributors and the open-source community for their valuable tools and libraries that made this project possible.
