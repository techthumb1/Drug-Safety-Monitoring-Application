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
├── backend/<br>
│   ├── manage.py<br>
│   ├── Pipfile<br>
│   ├── Pipfile.lock<br>
│   ├── .env<br>
│   ├── db.sqlite3<br>
│   ├── app/<br>
│   │   ├── __init__.py<br>
│   │   ├── settings/<br>
│   │   │   ├── base.py<br>
│   │   │   ├── development.py<br>
│   │   │   └── production.py<br>
│   │   ├── urls.py<br>
│   │   ├── wsgi.py<br>
│   │   └── ... (Additional Backend Components)<br>
│<br>
├── frontend/<br>
│   ├── package.json<br>
│   ├── package-lock.json<br>
│   ├── .env
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── ... (UI Components & Assets)
│
├── .gitignore
├── README.md
└── LICENSE

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

