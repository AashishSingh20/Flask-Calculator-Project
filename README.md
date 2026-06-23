# 🧮 Smart Calculator using Flask

A modern web-based calculator built with **Flask**, **HTML**, and **CSS**. This application performs basic arithmetic operations through an interactive user interface and also supports API testing through Postman.

---

## 🚀 Features

✅ Addition

✅ Subtraction

✅ Multiplication

✅ Division

✅ Clean and Responsive UI

✅ Flask Form Handling

✅ REST API Endpoint for Postman

✅ Result Page Display

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Jinja2

---

## 📂 Project Structure

```text
Flask-Calculator-Project/
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Flask-Calculator-Project.git
```

### Move into the Project Directory

```bash
cd Flask-Calculator-Project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

---

## 🌐 Access the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📸 Preview

### Home Page

- Enter two numbers
- Select an operation
- Click Calculate

### Result Page

- Displays the result of the selected operation
- Option to perform another calculation

---

## 🔌 API Testing with Postman

### Endpoint

```http
POST /postman_action
```

### Sample Request Body

```json
{
    "num1": 25,
    "num2": 5,
    "operation": "divide"
}
```

### Supported Operations

| Operation | Value |
|------------|---------|
| Addition | add |
| Subtraction | subtract |
| Multiplication | multiply |
| Division | divide |

---

## 📚 Concepts Practiced

- Flask Routing
- GET & POST Requests
- Form Handling
- Template Rendering
- Jinja2
- JSON Responses
- REST APIs
- Frontend & Backend Integration

---

## 🎯 Future Improvements

- User Authentication
- Calculation History
- Dark Mode
- Scientific Calculator Functions
- Database Integration

---

## 👨‍💻 Author

**Aashish Singh**

Computer Engineering Student | Machine Learning Enthusiast | Python Developer

---

⭐ If you like this project, consider giving it a star on GitHub!
