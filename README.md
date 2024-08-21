<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">SALON-MANAGEMENT</h1>
</p>
<p align="center">
    <img src="https://img.shields.io/github/license/techdev59/salon-management.git?style=flat&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/techdev59/salon-management.git?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/techdev59/salon-management.git?style=flat&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/techdev59/salon-management.git?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
        <em>Developed with the software and tools below.</em>
</p>
<p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=Django&logoColor=white" alt="Django">
    <img src="https://img.shields.io/badge/PostgreSQL-336791.svg?style=flat&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">

</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Getting Started](#-getting-started)
>   - [Environment Variables](#environment-variables)
>   - [ Installation](#-installation)
>   - [ Running salon-management](#-running-salon-management)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---
## Overview

This Salon Management System is a comprehensive solution designed to streamline and manage salon operations. Built with Django and GraphQL, the system offers dynamic database support for multiple salon branches, allowing each branch to maintain separate records while still being managed centrally. The platform provides tools for managing appointments, staff, services, and customer relationships, ensuring an efficient workflow and a smooth customer experience.

The system is designed with scalability and flexibility in mind, allowing for easy expansion as the business grows. It integrates seamlessly with other tools, offers secure authentication, and provides detailed reporting and analytics to help salon owners make data-driven decisions.

## Features

- **Multi-Salon Support**: Dynamically manage multiple salon branches, each with its own database for independent data management.
  
- **Appointment Scheduling**: Easily manage customer appointments, including booking, rescheduling, and cancellations, with support for multiple services and staff members.
  
- **Staff Management**: Keep track of staff members' schedules, roles, and availability. Assign tasks and manage shifts efficiently.
  
- **Service Management**: Manage and customize the list of services offered, including pricing, duration, and staff specialization.

- **Customer Relationship Management (CRM)**: Maintain detailed records of customers, including contact information, appointment history, and service preferences.
  
- **Payment and Billing**: Track payments, generate invoices, and manage billing for services provided at the salon.
  
- **Inventory Management**: Keep track of salon products and supplies, including automatic reminders for restocking.
  
- **Reporting and Analytics**: Generate reports on appointments, staff performance, revenue, and customer data to gain insights into salon operations.
  
- **User Authentication and Roles**: Secure login and role-based access control to manage permissions for staff and administrators.
  
- **Mobile-Friendly Interface**: A responsive and intuitive user interface that works well on both desktop and mobile devices.
  
- **Notifications and Reminders**: Automatic email and SMS notifications for appointment confirmations, reminders, and cancellations.
  
- **Customizable Settings**: Flexible settings that allow each salon branch to customize operational parameters, including business hours, service offerings, and pricing.

- **Secure and Scalable**: Designed with security best practices and scalability in mind to support future growth and expansion of the salon business.


---

##  Repository Structure

```sh
└── salon-management/
    ├── README.md
    ├── accounts
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── management
    │   │   ├── __init__.py
    │   │   └── commands
    │   │       ├── __init__.py
    │   │       └── init_salon.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── requirements.txt
    ├── salon
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── salon_management
        ├── __init__.py
        ├── asgi.py
        ├── db_routers.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

---


##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.12`

### Environment Variables

To configure the database and other project settings, you need to set up a `.env` file in the root of your project. Below is an example of the required environment variables:

### Example `.env` File

```bash
# General Settings
DEBUG=True
SECRET_KEY=your_secret_key_here

# Database Configuration for PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_database_name_here
DB_USER=your_database_user_here
DB_PASSWORD=your_database_password_here
DB_HOST=your_database_host_here
DB_PORT=5432  # Default PostgreSQL port


```

###  Installation

1. Clone the salon-management repository:

```sh
git clone https://github.com/techdev59/salon-management.git
```

2. Change to the project directory:

```sh
cd salon-management
```

3. Create virtual environment:

```sh
python -m venv venv
```

3. Activate virtual environment:

for wundows
```sh
venv\Scripts\activate
```
for linux
```sh
Source venv/bin/activate
```


4. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running salon-management

Use the following command to run salon-management:

```sh
python manage.py runserver
```


## To apply migrations 

first use this command

```sh
python manage.py makemigrations
```
then apply all the migrations
```sh
python manage.py migrate
```


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/techdev59/salon-management.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/techdev59/salon-management.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/techdev59/salon-management.git/issues)**: Submit bugs found or log feature requests for Salon-management.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/techdev59/salon-management.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

We would like to express our gratitude to the following resources and individuals for their support and contributions throughout the development of this Django project with GraphQL:

- **Django**: The Django Web Framework served as the foundation for our project, and its robust features and excellent documentation were invaluable. [Django](https://www.djangoproject.com/)

- **Django Packages**: Various Django packages, including `django-filter`, `django-cors-headers`, and others, helped make this project possible.

- **Community Support**: The contributions and guidance from the Django and GraphQL communities, especially the help provided on platforms like Stack Overflow and GitHub Discussions, were invaluable in overcoming challenges during development.

- **Open-Source Contributors**: We extend our thanks to the open-source contributors whose work made this project possible. Your code, libraries, and contributions to the ecosystem are deeply appreciated.

Thank you to everyone who helped make this project a reality. Your support and dedication are appreciated!

---
