### 🏡 California House Price Prediction App

### Software and tools needed

1. [GitHub](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

##  Features
✅ Predict house prices based on input features
✅ Built with Flask for a seamless web interface
✅ Machine Learning with Scikit-Learn (Linear Regression Model)
✅ Data processing with Pandas & NumPy
✅ Visualization with Matplotlib
✅ Gunicorn for production
✅ Containerized using Docker for portability
✅ CI/CD Pipeline with Heroku & Git for automated deployment

## Tech Stack
🔹 Backend: Flask, Python
🔹 Frontend: HTML, CSS
🔹 ML Model: Linear Regression (Scikit-Learn)
🔹 Data Handling: Pandas, NumPy
🔹 Visualization: Matplotlib
🔹 Deployment: Docker, Heroku, Gunicorn
🔹 Version Control & CI/CD: Git, GitHub Actions

To Create a New environment

```
conda create -p venv python -y
```

### How to Run Locally
1️⃣ Clone the repository:
```
git clone https://github.com/saivarma97/housepricing.git
cd repo-name
```

2️⃣ Install dependencies:
```
pip install -r requirements.txt
```

3️⃣ Run the Flask app:
```
python app.py
```

4️⃣ Open in the browser:
```
Open the Http link displayed (eg:http://127.0.0.1:5000)
```


## Here is the final HTML page with predicted value
User gives his values to get the Estimated price in california

![Here is the final HTML page with predicted value](image.png)

## Deployment

The app is deployed on Heroku using a CI/CD pipeline. Every push to the main branch automatically triggers a new deployment.