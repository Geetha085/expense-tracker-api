# Expense Tracker REST API

A backend RESTful API built using **Python** and **Django REST Framework** to manage daily expenses. The project demonstrates core backend concepts such as HTTP methods, REST APIs, JSON-based communication, and client–server architecture. It is designed as a beginner-to-intermediate level project and is fully deployable.

---

## Features

* Create a new expense
* Retrieve all expenses
* Filter expenses by category and date
* Update expense details (full and partial updates)
* Delete an expense
* JSON-based request and response handling

---

## Concepts Covered

* HTTP methods: GET, POST, PUT, PATCH, DELETE
* RESTful API design principles
* Client–server architecture
* JSON request and response lifecycle
* CRUD operations
* Query parameter filtering

---

## Tech Stack

* **Language:** Python
* **Framework:** Django, Django REST Framework
* **Database:** SQLite (can be upgraded to PostgreSQL)
* **API Testing:** Postman
* **Deployment:** Render

---

## Client–Server Architecture

```
Client (Postman / Browser)
        ↓ HTTP Request
Django REST API (Server)
        ↓ ORM
     Database
        ↑ JSON Response
```

---

## API Endpoints

| Action           | Method      | Endpoint                 |
| ---------------- | ----------- | ------------------------ |
| Create expense   | POST        | /expenses/               |
| Get all expenses | GET         | /expenses/               |
| Filter expenses  | GET         | /expenses/?category=Food |
| Update expense   | PUT / PATCH | /expenses/{id}/          |
| Delete expense   | DELETE      | /expenses/{id}/          |

---

## Sample JSON Requests

### Create Expense (POST)

```json
{
  "title": "Lunch",
  "amount": 150,
  "category": "Food",
  "date": "2026-01-27"
}
```

### Partial Update (PATCH)

```json
{
  "amount": 180
}
```

---

## Live Demo

🔗 Live API URL: [https://expense-tracker-api-7wtq.onrender.com/expenses/]

---

## Testing

* All APIs were tested using **Postman**
* Verified request payloads, responses, and HTTP status codes

---


