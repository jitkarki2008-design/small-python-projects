[README.md](https://github.com/user-attachments/files/30187092/README.md)
# 🐍 Small Python Projects

A collection of 10 beginner-to-intermediate Python projects, built to practice core concepts — from variables and loops to file handling, APIs, JSON, and OOP. Each project is a small, self-contained CLI tool..

## 📋 Projects Overview

| # | Project | Concepts | File |
|---|---------|----------|------|
| 01 | [CGPA Grade Checker](#01--cgpa-grade-checker) | variables, if-elif-else, f-strings | `grade.py` |
| 02 | [Smart Calculator](#02--smart-calculator) | functions, loops, try-except | `calc.py` |
| 03 | [Number Guessing Game](#03--number-guessing-game) | random, while loop | `guess.py` |
| 04 | [To-Do List CLI](#04--to-do-list-cli) | file handling | `todo.py` |
| 05 | [Expense Tracker](#05--expense-tracker) | dict, csv | `tracker.py` |
| 06 | [Password Generator](#06--password-generator) | string, random | `pass.py` |
| 07 | [Quiz App](#07--quiz-app) | json, random | `quiz.py` |
| 08 | [Weather App](#08--weather-app) | API, requests | `weather.py` |
| 09 | [Student Management System](#09--student-management-system) | OOP, json | `student.py` |
| 10 | [QR Code Generator](#10--qr-code-generator) | qrcode, Pillow | `qr.py` |

---

## 📦 Project Details

### 01 — CGPA Grade Checker
Takes a name and CGPA (0–10) and converts it into a percentage and letter grade, using VIT-AP's grading scale. Flags eligibility for a merit scholarship if CGPA ≥ 9.0.

```bash
python grade.py
```

### 02 — Smart Calculator
A menu-driven calculator supporting add, subtract, multiply, and divide, with safe handling of division by zero via `try/except`. Runs in a loop until the user exits.

```bash
python calc.py
```

### 03 — Number Guessing Game
The program picks a random number between 1 and 100 and the player tries to guess it, getting "too high / too low" hints. Tracks attempts and assigns a rank ("Pro Gamer", "Smart Player", "Keep Practicing") at the end.

```bash
python guess.py
```

### 04 — To-Do List CLI
A persistent to-do list that saves tasks to `tasks.txt`. Supports viewing, adding, and deleting tasks, and reloads existing tasks on startup.

```bash
python todo.py
```

### 05 — Expense Tracker
Logs expenses (date, category, amount, note) to `expenses.csv` using Python's `csv` module. Includes a summary view that totals spending overall and broken down by category.

```bash
python tracker.py
```

### 06 — Password Generator
Generates secure, customizable passwords using the `random` and `string` modules. Lets the user choose which character types to include (uppercase, lowercase, digits, symbols) and guarantees at least one of each selected type.

```bash
python pass.py
```

### 07 — Quiz App
A multiple-choice quiz that loads questions from `questions.json`, shuffles them each run, accepts answers by number or text, and reports a final score with percentage-based feedback.

```bash
python quiz.py
```

### 08 — Weather App
Fetches live weather data for any city using the free [wttr.in](https://wttr.in) API (no API key required) via the `requests` library. Displays temperature, "feels like," condition, humidity, and wind speed.

```bash
python weather.py
```

### 09 — Student Management System
An OOP-based CRUD system for managing student records, with a `Student` class and a `StudentManagementSystem` class handling persistence to `students.json`. Supports adding, viewing, searching, updating, and deleting students.

```bash
python student.py
```

### 10 — QR Code Generator
Generates a QR code from any text or URL using the `qrcode` and `Pillow` libraries, with customizable fill and background colors, and saves the result as a `.png` image.

```bash
python qr.py
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Standard Library:** `random`, `string`, `csv`, `json`, `os`, `datetime`
- **Third-party:** `requests`, `qrcode`, `Pillow`

## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/jitkarki2008-design/small-python-projects.git
cd small-python-projects

# Install dependencies (needed for the Weather App and QR Code Generator)
pip install requests qrcode pillow

# Run any project
python <filename>.py
```

## 📁 Repository Structure

```
small-python-projects/
├── grade.py               # 01 - CGPA Grade Checker
├── calc.py                # 02 - Smart Calculator
├── guess.py                 # 03 - Number Guessing Game
├── todo.py                 # 04 - To-Do List CLI
├── tracker.py              # 05 - Expense Tracker
├── pass.py                  # 06 - Password Generator
├── quiz.py                  # 07 - Quiz App
├── questions.json            # Quiz question bank
├── weather.py               # 08 - Weather App
├── student.py               # 09 - Student Management System
├── students.json             # Student records (auto-generated)
├── qr.py                     # 10 - QR Code Generator
└── README.md
```

## 🎯 What This Covers

Building these 10 projects touches on most of the Python fundamentals needed before moving into larger applications:

- Core syntax — variables, conditionals, loops, functions
- Error handling with `try/except`
- File I/O and data persistence (`.txt`, `.csv`, `.json`)
- Working with external APIs (`requests`)
- Object-Oriented Programming (classes, methods, encapsulation)
- Using third-party packages (`qrcode`, `Pillow`)

## 🙋 Author

**Jit Karki**
GitHub: [@jitkarki2008-design](https://github.com/jitkarki2008-design)

---

⭐ If you found this useful, consider giving the repo a star!
