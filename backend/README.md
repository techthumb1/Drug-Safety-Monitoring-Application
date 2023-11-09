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