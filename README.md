
# **README — Module 4 Project**  
Grant Eberhardt  
Study Tracker API • API Exploration + API Design

---

## **📌 Overview**

This project is divided into two major parts:

1. **API Exploration** — A Python script that explores three real public APIs using live HTTP requests.  
2. **Study Tracker API Design** — A full REST API specification including resources, relationships, endpoints, schemas, authentication, and error handling.

This README explains the purpose of each part, summarizes the APIs explored, and documents the full design of the Study Tracker API.

---

# **Part 1 — API Exploration**

The `explorer.py` script interacts with three public APIs:

- **JSONPlaceholder** — Fake REST API for testing  
- **PokeAPI** — Pokémon data API  
- **REST Countries** — Country and region data

The script demonstrates:

- GET requests  
- POST requests  
- Query parameter filtering  
- Nested resources  
- Error handling  
- JSON parsing and summarization  

---

## **🔎 API 1 — JSONPlaceholder**

**Base URL:** [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)  
**Auth:** None

### Endpoints Explored

#### **GET /users**
Retrieves a list of 10 user objects.

```json
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "email": "Sincere@april.biz"
  }
]
```

#### **GET /posts?userId=5**
Server‑side filtering using query parameters.

#### **POST /posts**
Simulated resource creation. Always returns `id: 101`.

### Observations
- No rate limits encountered  
- POST always returns the same ID because data is not persisted  
- Useful for practicing REST patterns  

---

## **🔎 API 2 — PokeAPI**

**Base URL:** [https://pokeapi.co/api/v2](https://pokeapi.co/api/v2)  
**Auth:** None

### Endpoints Explored

#### **GET /pokemon/1**
Bulbasaur details (height, weight, abilities).

#### **GET /pokemon/25**
Pikachu details.

#### **GET /type/<id>**
Nested resource: Pokémon → Type → Pokémon list.

#### **GET /pokemon-species/<id>**
Nested resource: Pokémon → Species.

### Observations
- Nested URLs feel like relational database foreign keys  
- Occasional slowdowns but no hard rate limits  
- Very consistent JSON structure across Pokémon IDs  

---

## **🔎 API 3 — REST Countries (Mirror API)**

**Base URL:** [https://restcountries.com/v3.1](https://restcountries.com/v3.1)  
**Auth:** None

### Endpoints Explored

#### **GET /name/japan?fullText=true**
Country details including capital, population, region.

#### **GET /region/europe**
List of European countries.

#### **GET /name/notacountry**
Intentional error test.

### Observations
- Some endpoints deprecated  
- Mirror endpoints still reliable  
- Error responses vary depending on endpoint  

---

# **Part 2 — Study Tracker API Design**

The Study Tracker API helps students log study sessions, set weekly goals, and track progress.

---

## **📚 Resources**

- Students  
- Courses  
- Study Sessions  
- Goals  
- Progress Summaries  

Each resource includes structured attributes such as IDs, timestamps, durations, and weekly metrics.

---

## **🔗 Relationships**

- Student ↔ Course: many‑to‑many  
- Student ↔ Study Session: one‑to‑many  
- Course ↔ Study Session: one‑to‑many  
- Student ↔ Goal: one‑to‑many  
- Course ↔ Goal: one‑to‑many  
- Student ↔ Progress Summary: one‑to‑many  

This structure supports filtering, aggregation, and weekly progress reporting.

---

## **🛠 Endpoint List (12 total)**

### Study Sessions (CRUD)
- POST /studysessions  
- GET /studysessions  
- GET /studysessions/{id}  
- PUT /studysessions/{id}  
- DELETE /studysessions/{id}  

### Related Resources
- GET /students  
- GET /courses  
- POST /goals  
- GET /progress_summaries  

### Filtering
- GET /studysessions?course_id={id}  
- GET /studysessions?student_id={id}  
- GET /studysessions?week_start={date}  

---

## **📄 Request/Response Schemas**

### POST /study_sessions — Request
```json
{
  "student_id": "integer",
  "course_id": "integer",
  "duration_minutes": "integer",
  "notes": "string",
  "timestamp": "datetime"
}
```

### GET /students/{id}/progress — Response
```json
{
  "student_id": "integer",
  "summaries": [
    {
      "course_id": "integer",
      "week_start_date": "date",
      "total_hours_studied": "float",
      "target_hours": "integer",
      "completion_percentage": "float",
      "sessions_count": "integer",
      "status": "string"
    }
  ]
}
```

---

## **🔐 Authentication Plan**

### Method
JWT Bearer Token authentication.

### Public Endpoint
- GET /courses

### Protected Endpoints
- POST /study_sessions  
- GET /students/{id}/progress  
- DELETE /study_sessions/{id}  

### Role Matrix

| Endpoint | Student | Instructor | Admin |
|---------|---------|------------|-------|
| GET /courses | Allowed | Allowed | Allowed |
| POST /study_sessions | Allowed | Not allowed | Allowed |
| GET /students/{id}/progress | Own only | Students they teach | Allowed |
| DELETE /study_sessions/{id} | Not allowed | Students they teach | Allowed |

---

## **⚠ Error Responses (POST /study_sessions)**

| Status | Meaning |
|--------|---------|
| 201 Created | Resource successfully created |
| 400 Bad Request | Missing or invalid fields |
| 401 Unauthorized | Missing/invalid JWT |
| 404 Not Found | Student/course/session not found |
| 422 Unprocessable Entity | Semantically invalid data |

---

# **📌 Final Notes**

This project demonstrates:

- Real API exploration  
- Understanding of REST patterns  
- Full API design including resources, relationships, endpoints, schemas, authentication, and error handling  

