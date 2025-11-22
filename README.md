# 📘 Results Management System – Simple Guide

This is a simple Flask-based Results Management System, created for students who are learning Python, Flask, and basic web development.

Teachers can:
- Manage students
- Manage classes
- Manage subjects
- Assign marks

Students can:
- Search for their results using roll number and class

This project intentionally avoids advanced/complex features so that beginners can understand everything easily.

This guide will help you **run the project step-by-step**, even if you are new to Python.

---

## 🚫 What We Did Not Use (To Keep It Simple)

To keep this project beginner-friendly, we avoided:

❌ Complex components like jQuery / AJAX for partial page updates

❌ Password hashing (plain text is used for learning only)

❌ Responsive UI (basic Bootstrap only)

❌ Dark theme / theme switching

❌ Advanced session-based menu updates (no dynamic menu based on login status)

❌ API routes or JavaScript-heavy frontend

❌ Role-based permissions

This project is focused on understanding basic Flask, not on building a production system.

---

## ✅ 1. Install Python

Download and install Python from:

👉 https://www.python.org/downloads/

Make sure to check the box **“Add Python to PATH”** during installation.

---

## ✅ 2. Create Virtual Environment

Open your terminal inside the project folder, then run:

```bash
python -m venv venv
```


This will create a virtual environment named **venv**.

---

## ✅ 3. Activate Virtual Environment

### ▶️ For Windows

```bash
.\venv\Scripts\activate
```


### ▶️ For Linux/Mac

```bash
source venv/bin/activate
```

You should now see `(venv)` at the start of your terminal line.

---

## ✅ 4. Install Required Libraries

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## ✅ 5. Create Admin User (Only First Time)

Before running the project for the first time, create an admin account by running:

```bash
python seed.py
```

This step is required **only once**.

---

## ✅ 6. Run the Project

Start the Flask application using:

```bash
python app.py
```


You will see something like:

```bash
Running on http://127.0.0.1:5000
```

Open the link in your browser.

---

Use the admin credentials created by **seed.py**.

---

## 🎉 Done!

Your Results Management System is now up and running.
