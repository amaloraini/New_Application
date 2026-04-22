# Aura - Premium E-Commerce Platform

Aura is a modern, deployable e-commerce web application built with Flask and Python. It features a premium, responsive dark-mode design with glassmorphism aesthetics and smooth micro-animations.

## Features
- **Modern UI**: Clean, premium design focusing on visual excellence using modern fonts (Inter) and custom properties.
- **Glassmorphism Design**: Semi-transparent cards with backdrop filters that react smoothly to user interactions.
- **Interactive Cart**: Functional offcanvas shopping cart utilizing Javascript for state management.
- **Responsive**: Fully mobile-compatible, adjusting layout seamlessly on smaller screens.
- **API Endpoints**: RESTful structure for fetching products and adding to cart (Simulated in the backend).
- **Deployment Ready**: Fully configured with `gunicorn` in `requirements.txt` and a declarative `Procfile`.

## Tech Stack
- **Backend**: Python 3, Flask
- **Frontend**: HTML5, Vanilla CSS, Vanilla JavaScript
- **Server**: Gunicorn (for production WSGI serving)

## Running Locally

1. **Navigate to the project directory:**
   Ensure you are in the application folder:
   ```bash
   cd New_Application
   ```

2. **Create a virtual environment (Optional but highly recommended):**
   ```bash
   python -m venv venv
   # On Windows use:
   venv\Scripts\activate
   # On Mac/Linux use:
   # source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Open your browser:** 
   Visit `http://127.0.0.1:5000` to view the application in action.

## Deployment

This application is structurally prepared to be deployed to platforms like Heroku, Render, or any cloud platform that supports standard Python web applications.

### Heroku Deployment Example:
1. Ensure you have the Heroku CLI installed on your machine.
2. Login to Heroku via terminal: `heroku login`
3. Initialize git if you haven't already: 
   ```bash
   git init
   git add .
   git commit -m "Initial commit for production"
   ```
4. Create a new Heroku application: 
   ```bash
   heroku create your-unique-app-name
   ```
5. Push your code to the Heroku remote: 
   ```bash
   git push heroku main
   ```

The included `Procfile` correctly instructs Heroku to use `gunicorn` to serve the Flask application (`web: gunicorn app:app`).
