# Drug-Safety-Monitoring-Application

Drug Safety Monitoring App

Welcome to the Drug Safety Monitoring App, a holistic solution designed to augment and streamline pharmacovigilance through the power of AI. By integrating deep learning, machine learning, and a seamless web interface, our tool aids professionals in the biopharmaceutical domain to predict and monitor drug safety based on user reviews.

[] App Screenshot <!-- Add screenshot of the app -->

## Table of Contents

- Features
- Directory Structure
- Getting Started
- Tech Stack
- Roadmap
- Contributing
- License

## Features

- **Review Input Interface**:** Seamlessly enter and manage drug reviews.
- **Safety Prediction**: Advanced deep learning models offer predictions regarding drug safety based on reviews.
- **Interactive Visualizations**: Extract insights from rich, interactive charts and plots related to drug reviews.
- **Database Management**: Integrated with PostgreSQL, ensuring reliable and efficient data handling.
- **Responsive UI**: Engage with a user-friendly and adaptive interface.

## Directory Structure

DrugSafetyMonitoringApp/<br>
│<br>
├── backend/ # Backend-related files<br>
│ ├── app.py # Flask application entry point<br>
│ ├── Pipfile # Pipenv file for dependency management<br>
│ ├── Pipfile.lock # Pipenv lock file to ensure deterministic builds<br>
│ ├── .env # Environment variables file<br>
│ ├── db.sqlite3 # SQLite database for development<br>
│ ├── models/ # Database models<br>
│ │ ├── init.py<br>
│ │ ├── drug_review.py # Model for drug reviews<br>
│ │ └── ...<br>
│ ├── services/ # Business logic<br>
│ │ ├── init.py<br>
│ │ ├── review_service.py # Service for review processing<br>
│ │ └── ...<br>
│ ├── static/ # Static files<br>
│ │ ├── css/<br>
│ │ │ └── main.css # Main stylesheet<br>
│ │ ├── js/<br>
│ │ │ └── main.js # Main JavaScript file<br>
│ │ └── images/<br>
│ ├── templates/ # Jinja2 templates<br>
│ │ ├── base.html # Base template<br>
│ │ ├── index.html # Index page template<br>
│ │ └── ...<br>
│ ├── routes/ # Web routes<br>
│ │ ├── init.py<br>
│ │ ├── main_routes.py # Main routes for the application<br>
│ │ └── api_routes.py # API routes<br>
│ ├── ml_models/ # Machine Learning models<br>
│ │ ├── init.py<br>
│ │ ├── review_processor.py # Review processing utilities<br>
│ │ └── drug_safety_model.h5 # Trained ML model for predictions<br>
│ └── config.py # Configuration settings<br>
│<br>
├── frontend/ # Frontend-related files<br>
│ ├── package.json # Node.js package definition<br>
│ ├── package-lock.json # Node.js locked dependencies<br>
│ ├── .env # Frontend environment variables<br>
│ ├── public/<br>
│ │ └── index.html # HTML entry point<br>
│ ├── src/<br>
│ │ ├── App.js # Main React/Vue application file<br>
│ │ ├── index.js # JavaScript entry point<br>
│ │ └── ...<br>
│ └── ...<br>
│<br>
├── .gitignore # Specifies intentionally untracked files to ignore<br>
├── README.md # The file you're reading right now<br>
└── LICENSE # Legal terms of use<br>

## Getting Started

Clone the repository:

```bash
git clone https://github.com/your_username/DrugSafetyMonitoringApp.git
```

Setup the backend:

```bash
cd DrugSafetyMonitoringApp/backend
pipenv install
pipenv shell
flask db upgrade
```

Setup the frontend:

```bash
cd DrugSafetyMonitoringApp/frontend
npm install
npm start
```

## Tech Stack

- Backend: Flask, PostgreSQL
- Frontend: React, Material UI, Plotly.js, Axios, React Router, React Bootstrap, 
HTML, CSS, JavaScript
- ML/AI: TensorFlow, Keras, Scikit-learn, SpaCy

## Roadmap

- Integrate React-based frontend for dynamic UI experience.
- Develop RESTful APIs for enhanced communication between frontend and backend.
- Incorporate detailed drug analytics based on biopharmaceutical parameters.
- Add user authentication and role-based access control.
- Implement CI/CD pipelines for automated testing and deployment.

## Contributing

Open to contributions! Whether it's bug fixes, feature suggestions, or documentation improvements, every bit helps. Kindly refer to the CONTRIBUTING.md file for guidelines.

## License

MIT License. Check the [LICENSE](https://github.com/techthumb1/Drug-Safety-Monitoring-Application/blob/main/LICENSE) file for detailed information.

