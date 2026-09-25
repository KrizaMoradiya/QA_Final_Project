# QA Automation Final Project

## Overview

This project is a basic QA automation framework created using Python, Pytest, Playwright, Page Object Model (POM), API Testing, SQL/SQLite, and HTML Test Reports.

The project demonstrates the complete QA testing workflow:

Requirement → Test Case → UI Automation → API Validation → Database Validation → Test Report → GitHub

---

## Requirement

The application should allow users to log in successfully using valid username and password.

If invalid login credentials are entered, an appropriate error message should be displayed.

---

## Test Cases

### UI Login Test Cases

- TC01 - Valid username and valid password
- TC02 - Invalid username
- TC03 - Invalid password
- TC04 - Empty username
- TC05 - Empty password

### API Test Cases

- Validate GET Users API response
- Validate User API response fields

### Database Test Case

- Validate that the user exists in the database

---

## Application Used

### UI Application

SauceDemo

URL:

https://www.saucedemo.com/

Test Credentials:

Username: standard_user

Password: secret_sauce

### API

JSONPlaceholder

Base URL:

https://jsonplaceholder.typicode.com

### Database

SQLite

---

## Technologies Used

- Python
- Pytest
- Playwright
- Page Object Model (POM)
- Postman
- Requests
- SQL
- SQLite
- pytest-html
- Git
- GitHub

---

## Project Structure

QA_Final_Project/

├── pages/

│   └── login_page.py

├── tests/

│   ├── test_login.py

│   ├── test_api.py

│   └── test_database.py

├── utils/

│   └── helpers.py

├── test_data/

│   └── login_data.json

├── reports/

│   └── report.html

├── conftest.py

├── requirements.txt

├── pytest.ini

├── README.md

└── .gitignore

---

## UI Automation

Playwright is used to automate the SauceDemo login functionality.

The Page Object Model is used to separate page locators and page actions from test cases.

The login page contains:

- Username field
- Password field
- Login button

The automated tests validate both successful and unsuccessful login scenarios.

---

## API Testing

API testing is performed using:

- Postman for manual API validation
- Python Requests library for automated API testing
- Pytest for API assertions

The following validations are performed:

- HTTP status code
- Response type
- Response data
- Required response fields

---

## Database Validation

SQLite is used for database validation.

The test creates a users table and validates that the expected user exists in the database.

SQL query used for validation:

SELECT username
FROM users
WHERE username = 'standard_user';

---

## Test Execution

First activate the virtual environment:

```bash
source .venv/bin/activate