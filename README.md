# 🚇 CrowdFlow AI

### Machine Learning-Based Passenger Demand Prediction for London Public Transport

CrowdFlow AI is a machine learning-powered web application designed to predict passenger demand across London's public transport network using historical Transport for London (TfL) NUMBAT data.

The system uses a **Random Forest regression model** to analyse journey information such as origin station, destination station, Underground line, direction, day type and travel time.

Users can enter their journey details through a Flask-based web interface and receive:

- 📊 Estimated passenger demand
- 🚦 Crowd level classification
- 💡 Travel guidance based on predicted demand

## 🔗 Live Project

**Live Demo:** https://crowdflow-ai-8f85.onrender.com

**GitHub Repository:** You are currently viewing the source code for CrowdFlow AI.
## 🛠️ Tech Stack

### Backend & Machine Learning
- **Python** – Core programming language
- **Flask** – Web application framework
- **Scikit-learn** – Machine learning model development
- **Random Forest Regressor** – Passenger demand prediction
- **Pandas** – Data preprocessing and manipulation
- **Joblib** – Model serialization and loading

### Frontend
- **HTML5**
- **CSS3**
- **Jinja2**

### Development & Deployment
- **Git & GitHub** – Version control and source code management
- **Render** – Cloud deployment
- **Gunicorn** – Production WSGI server

### Data
- **TfL NUMBAT** – Historical London public transport passenger demand data
