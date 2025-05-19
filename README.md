# flashcard_backend-

# 📚 Flashcard API - Mixed Subjects

This is a simple REST API that returns flashcards from different subjects for a specific student. It ensures that the flashcards are shuffled and limited to the number requested.

---

## 🚀 Endpoint

### `GET /get-subject`

Returns flashcards belonging to a student, from various subjects, shuffled and limited by your input.

---

### 🔸 Query Parameters

| Parameter    | Type   | Required | Description                              |
|--------------|--------|----------|------------------------------------------|
| `student_id` | string | ✅       | The ID of the student                    |
| `limit`      | int    | ❌       | Maximum number of flashcards to return (default is 5) |

---

### ✅ Example Request

---

### 📤 Sample Response

```json
[
  {
    "question": "What is Newton's Second Law?",
    "answer": "Force equals mass times acceleration",
    "subject": "Physics"
  },
  {
    "question": "What is photosynthesis?",
    "answer": "A process used by plants to convert light into energy",
    "subject": "Biology"
  }
]

🛠️ Technologies Used
Node.js / Express.js or Python / Flask (use your preferred backend)

REST API principles

JSON


# 📚 Flashcard Backend

A simple backend service for managing flashcards.

---

## ✨ Features

- ✅ CRUD operations for flashcards  
- ✅ JSON data storage (or connect your own database)  
- ✅ RESTful API endpoints (if applicable)  
- ✅ Built with Python (or your preferred tech stack)  

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.x installed
- Required packages listed in `requirements.txt`

---

### 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/saikrishna770/flashcard-backend.git
cd flashcard-backend
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the App
bash
Copy
Edit
python app.py



📁 Project Structure (optional)
pgsql
Copy
Edit
flashcard-backend/
│
├── app.py
├── requirements.txt
├── data/                # (if applicable - for JSON storage)
└── README.md


🛠️ Tech Stack

Python 3.x

Flask / FastAPI (specify which you're using)

JSON (as simple data store)
