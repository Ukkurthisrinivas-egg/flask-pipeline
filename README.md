# Job-Ready Flask Application with Docker

This is a simple, professional web application built using **Flask** and containerized using **Docker**, with basic CI test integration. It's designed to demonstrate a full deployment pipeline — perfect for showcasing in a job application or technical assignment.

---

## 📁 Project Structure

```
job-ready-flask/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── run.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- Flask web application
- Docker containerization
- Pytest unit testing
- Simple REST route
- Clean folder structure
- Ready for CI tools (e.g., Trivy, SonarQube, OWASP later)

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourname/job-ready-flask.git
cd job-ready-flask
```

### 2. Create and activate a virtual environment (local)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🐳 Using Docker (Recommended for Production)

### 1. Build the container

```bash
docker-compose build
```

### 2. Run the application

```bash
docker-compose up
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Run Tests

### Run with Docker:

```bash
docker-compose run --rm web pytest
```

---

## 📬 API Route

| Method | Endpoint | Description       |
|--------|----------|-------------------|
| GET    | `/`      | Returns "Hello, World!" |

---

## ✅ To-Do (Optional Enhancements)

- Add Trivy for container vulnerability scanning
- Integrate SonarQube for code quality
- Add OWASP Dependency-Check
- Set up GitHub Actions CI/CD
- Add a frontend (e.g., React) or database if needed

---

## 🧑‍💻 Author

- Name: **Your Name**
- Email: your.email@example.com
- GitHub: [yourusername](https://github.com/yourusername)

---