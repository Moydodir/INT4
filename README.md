# Project Overview

This project is a web application built with a Docker container, serving static assets and HTML templates for a simple web interface.

## Project Structure
<pre>
docker
├── Dockerfile # Docker configuration to containerize the application
├── __init__.py # Initializes the application package
├── requirements.txt # Python dependencies
├── static # Folder for static files (images, CSS)
│   ├── main.jpg
│   └── style.css
└── templates # HTML templates for web pages
    ├── base.html
    └── card.html
</pre>

## Technologies Used

- **Python**: The main programming language.
- **Flask**: Web framework for building the application.
- **Jinja**: Templating engine used for rendering HTML.
- **HTML**: Markup language used for structuring web content.
- **Docker**: For containerization of the application.

## Getting Started

1. **Build Docker Image**:
   ```bash
   docker build -t myapp .
2. **Run Application**:
   ```bash
   docker run -p 5000:5000 myapp
3. **follow the path**:
   ```bash
   http://127.0.0.1:5000/healthz
## ⚠️ Warning
**the server will only respond to the request /healthz**

