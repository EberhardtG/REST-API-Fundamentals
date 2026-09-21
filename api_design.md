# Module 4 Project — Part 2: Study Tracker API Design

Grant Eberhardt
09/21/2026

---

## The App: Study Tracker

The Study Tracker app helps students log their study sessions, set weekly study goals for each course, and monitor their progress over time. It provides structured endpoints for recording session details, tracking target hours, and generating summaries that show how well students are meeting their goals. The API supports clear, organized study management so learners can stay consistent and improve their study habits.

---

## Section 1 — Resources

List the resources your API will manage. Suggested: Students, Courses, Study Sessions, Goals.

| Resource           | Key Attributes                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Students           | id, name, email, major (optional), year (optional)                                                                       |
| Courses            | id, course_name, course_code, instructor, credit_hours                                                                   |
| Study Sessions     | id, student_id, course_id, duration_minutes, notes, timestamp                                                            |
| Goals              | id, student_id, course_id, target_hours_per_week, week_start_date                                                        |
| progress summaries | student_id, course_id, week_start_date, total_hours_studied, target_hours, completion_percentage, sessions_count, status |

---

## Section 2 — Relationships

Describe how your resources relate to each other:

- Student ↔ Course: many-to-many
- Student ↔ Study Session: one-to-many
- Course ↔ Study Session: one-to-many
- Student ↔ Goal:one-to-many
- Course ↔ Goal: one-to-many
- Student ↔ Progress Summary:one-to-many
- Course ↔ Progress Summary: one-to-many

---

## Section 3 — Endpoints

Design at least:

- Full CRUD for study_sessions (5 endpoints)
- 3+ endpoints for related resources
- 1+ filtering endpoint

| Method                             | URI                                       | Description | Auth Required? |
| ---------------------------------- | ----------------------------------------- | ----------- | -------------- |
| Method                             | URI                                       | Description | Auth Required? |
| ---                                | ---                                       | ---         | ---            |
| **POST** [ /studysessions ]        | Create a new study session                | yes         |
| **GET** [ /studysessions ]         | Retrieve all study sessions               | yes         |
| **GET** [ /studysessions/{id} ]    | Retrieve a single study session by its ID | yes         |
| **PUT** [ /studysessions/{id} ]    | Update an existing study session          | yes         |
| **DELETE** [ /studysessions/{id} ] | Delete a study session                    | yes         |

Related resources table:
| Method | URI | Description | Auth Required? |
| --- | --- | --- | --- |
| GET | /students | List all students | yes |
| GET | /courses | List all courses | No |
| POST | /goals | Create a weekly study goal | yes |
| GET | /progress_summaries | View weekly progress summaries | yes |

Filtering:
| Method | URI | Description | Auth Required? |
| --- | --- | --- | --- |
| GET | /studysessions?course_id={id} | Filter study sessions by course | yes |
| GET |/studysessions?student_id={id} | Filter study sessions by student | yes|
| GET | /studysessions?week_start={date}|Filter study sessions by date|yes|

---

## Section 4 — Request/Response Schemas

### POST /study_sessions — Create a new session

**Request body:**

```json
{
  "student_id": "integer, required",
  "course_id": "integer, required",
  "duration_minutes": "integer, required",
  "notes": "string, optional",
  "timestamp": "datetime (ISO 8601), required"
}
```

**Success response (201):**

```json
{
  "id": 42,
  "student_id": 1,
  "course_id": 101,
  "duration_minutes": 60,
  "notes": "Reviewed chapter 3 and completed practice problems",
  "timestamp": "2026-09-21T14:30:00Z",
  "created_at": "2026-09-21T14:31:00Z"
}
```

### GET /students/{id}/progress

**Response (200):**

````json
{
  "student_id": "integer",
  "summaries": [
    {
      "course_id": "integer",
      "week_start_date": "date (YYYY-MM-DD)",
      "total_hours_studied": "float",
      "target_hours": "integer",
      "completion_percentage": "float",
      "sessions_count": "integer",
      "status": "string"
    }
  ]
}

```json

#**POST/goals:**
{
  "student_id": "integer, required",
  "course_id": "integer, required",
  "target_hours_per_week": "integer, required",
  "week_start_date": "date (YYYY-MM-DD), required"
}

**Success Response (201)**
{
  "id": "integer",
  "student_id": "integer",
  "course_id": "integer",
  "target_hours_per_week": "integer",
  "week_start_date": "date",
  "created_at": "datetime"
}

````

**GET /studysessions/{id} — Retrieve a single study session**

Response (200)
{
"id": "integer",
"student_id": "integer",
"course_id": "integer",
"duration_minutes": "integer",
"notes": "string",
"timestamp": "datetime",
"created_at": "datetime"
}

---

## Section 5 — Authentication

| Endpoint                    | Auth Required                                            | Notes                             |
| --------------------------- | -------------------------------------------------------- | --------------------------------- |
| GET /courses no             | anyone can browse courses as they are publicly available |
| POST /study_sessions        | yes                                                      | may contain personal student info |
| GET /students/{id}/progress | yes                                                      | role based accessed required      |
| DELETE /study_sessions/{id} | yes                                                      | role based auth required          |

**Auth method and rationale:**

> Here’s a **clean, complete, assignment‑ready Authentication Plan** that meets _all_ three required criteria:

- **Which method?**
- **Which endpoints are public vs. protected?**
- **Who can access what?**

No Guided Links, no extra markup — just the polished text you can paste directly into your documentation.

---

## **Authentication Plan**

### **Authentication Method**

This API uses **JWT Bearer Token authentication**.  
Clients must include a valid token in the `Authorization: Bearer <token>` header when accessing protected endpoints. JWTs allow the server to verify identity and role (student, instructor, admin) without storing session state.

---

### **Public vs. Protected Endpoints**

**Public Endpoints (no authentication required):**

- `GET /courses` — Courses are publicly available and contain no sensitive information.

**Protected Endpoints (authentication required):**

- `POST /study_sessions` — Creating a study session involves personal academic activity and must be tied to an authenticated student or admin.
- `GET /students/{id}/progress` — Contains private study history and performance data; requires authentication and role validation.
- `DELETE /study_sessions/{id}` — Deleting study data is sensitive and restricted to authorized roles.

---

### **Role‑Based Access Control (Who can access what)**

**Students**

- Can create their own study sessions.
- Can view their own progress summaries.
- Cannot delete study sessions created by others.

**Instructors**

- Can view progress for students they teach.
- Can delete study sessions for students they supervise.
- Cannot create study sessions for themselves unless also registered as students.

**Admins**

- Full access to all endpoints.
- Can create, view, and delete any study session.
- Can view progress for any student.

---

### **Rationale**

Authentication protects sensitive academic data and ensures that only authorized users can modify or view private study information. Public endpoints remain open to support general browsing, while protected endpoints enforce identity and role checks to maintain data integrity and privacy.

| Endpoint                    | Student                  | Instructor                        | Admin   |
| --------------------------- | ------------------------ | --------------------------------- | ------- |
| GET /courses                | Allowed                  | Allowed                           | Allowed |
| POST /study_sessions        | Allowed                  | Not allowed                       | Allowed |
| GET /students/{id}/progress | Allowed (only their own) | Allowed (for students they teach) | Allowed |
| DELETE /study_sessions/{id} | Not allowed              | Allowed (for students they teach) | Allowed |

## Section 6 — Error Responses for POST /study_sessions

| Status Code                  | When it occurs                                                                                                               |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **201 Created**              | A new study session is successfully created.                                                                                 |
| **400 Bad Request**          | The client sends invalid data (missing required fields, wrong types, invalid date format).                                   |
| **401 Unauthorized**         | The client attempts to access a protected endpoint without a valid JWT token.                                                |
| **404 Not Found**            | The referenced resource does not exist (invalid student ID, course ID, or session ID).                                       |
| **422 Unprocessable Entity** | The request is well‑formed but contains semantically invalid data (negative duration, invalid week range, target hours < 0). |
