# Isabelle's Baptism Website

## Overview
This repository contains a Flask-based web application designed for Isabelle's baptism event. The website serves as an information hub, providing event details, RSVP functionality, and interactive elements for guests. The project employs modern web technologies, including HTML, CSS (SASS), JavaScript, and Python.

## Important Note ⚠️
**This application will NOT run until you change the database configuration and set up the database correctly!** Please make sure to update the required line in `app.py` and configure the database before running the project—e.g. this line:
```
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://user:password@localhost/invitees'
```

## Features
- **Event Information Page**: Displays details about the baptism ceremony and reception.
- **RSVP System**: Allows guests to register their attendance through an interactive form.
- **Dynamic Dropdowns**: JavaScript functionality dynamically adjusts form options based on user selections.
- **Responsive Design**: Utilizes CSS Grid and SASS to provide a mobile-friendly experience.
- **Flask Backend**: Manages routing and form submissions using Python.
- **Heroku Deployment Support**: Includes necessary files for deployment on Heroku.

## Project Structure
```
├── instance/          # Flask instance folder (e.g., database, sensitive data)
├── static/            # Contains CSS, JavaScript, and images
│   ├── css/           # Stylesheets (SASS compiled CSS)
│   ├── js/            # JavaScript files
│   └── images/        # Event-related images
├── templates/         # HTML templates for Flask rendering
│   ├── index.html     # Main landing page
│   ├── rsvp.html      # RSVP form page
│   ├── confirmation.html # Confirmation page after RSVP submission
├── virtual/           # Virtual environment (not included in Git)
├── .gitignore         # Files and directories to be ignored by Git
├── Procfile           # Defines startup command for Heroku deployment
├── app.py             # Main Flask application logic
├── info.txt           # Additional project information
├── readme.md          # Documentation file (this file)
├── requirements.txt   # Dependencies for the project
├── runtime.txt        # Specifies the Python version for Heroku
```

## Installation & Setup
### Prerequisites
Ensure you have Python installed on your system (recommended: Python 3.8+).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/semajrd1/isabelles_baptism_website.git
   cd isabelles_baptism_website
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv virtual
   source virtual/bin/activate   # On macOS/Linux
   virtual\Scripts\activate      # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Update the database configuration before running the app!**
5. Run the application from the terminal (where XXXX is your desired port):
   ```bash
   flask run -p XXXX
   ```
   
## Deployment
### Deploying to Heroku
1. Ensure you have the Heroku CLI installed.
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create
   ```
4. Add a remote repository:
   ```bash
   git remote add heroku https://git.heroku.com/your-app-name.git
   ```
5. Deploy the app:
   ```bash
   git push heroku main
   ```
6. Open the application:
   ```bash
   heroku open
   ```

## Technologies Used
- **Frontend:** HTML, CSS (SASS), JavaScript
- **Backend:** Flask (Python), Jinja2 templating
- **Database:** SQLite (optional for storing RSVPs)
- **Hosting:** Heroku

## Future Improvements
- Add email notifications for RSVP confirmations.
- Implement a database to store guest RSVP responses.
- Enhance accessibility and UI design.
- Integrate Google Maps for event location display.

## Contribution Guidelines
If you would like to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Open a pull request for review.

## Contact
For any questions or suggestions, feel free to reach out to [your email or GitHub profile].

---
### Demo
Watch the project demo: [![YouTube Video](https://img.shields.io/badge/YouTube-Watch-red?style=for-the-badge&logo=youtube)](https://youtu.be/XqzLDb11Exk)
